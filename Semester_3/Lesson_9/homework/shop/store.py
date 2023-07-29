import sqlite3
import re
import pandas as pd

from datetime import datetime

from utils import (
    AuthRequired,
    make_password,
    get_user,
    PASSWORD_PATTERN,
    EMAIL_PATTERN,
    EXPIRATION_DATE_PATTERN,
    CARD_CODE_PATTERN,
)


class Store:
    """
    Represents a store.
    """

    def __init__(
        self,
        con: sqlite3.Connection,
        first_name: str,
        last_name: str,
        password: str,
        email: str,
    ) -> None:
        """
        Initializes a Store instance.
        """
        self.con = con
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email

    def update_card(self, card_code: str, date: str, balance: float | int) -> None:
        """
        Updates card values.
        """
        # Empty message if values are empty
        if not card_code and date and balance:
            return "Empty values were given."

        # Check balance for ValueError
        try:
            balance = float(balance)
        except ValueError as error:
            return error

        # Create cursor from self.con - sqlite3.Connection()
        cursor = self.con.cursor()
        # Getting user by email and password
        user_message = get_user(cursor, self.email, self.password)
        # Raise AuthRequired exception if user does not exist
        if user_message is None:
            raise AuthRequired

        # Request to database for identical card code
        code = cursor.execute(
            """
            SELECT card_code FROM user
            WHERE email != ?
            and password != ?
            and card_code = ?
            """,
            (self.email, self.password, card_code),
        ).fetchall()

        # Check warning message for card code and card date are not valid
        if not (
            re.match(CARD_CODE_PATTERN, card_code)
            and re.match(EXPIRATION_DATE_PATTERN, date)
            and balance > 0
        ):
            return "Wrong credentials were given."
        # Check card code used by another user
        elif code:
            return (
                "Card has already used by another user, please check your card options!"
            )

        # Update user card values
        cursor.execute(
            """
            UPDATE user 
            SET
                card_code = ?,
                card_balance = ?,
                expiration_date = ?
            WHERE 
                email = ?
                and password = ?
            """,
            (card_code, round(balance, 2), date, self.email, self.password),
        )
        # Save changes
        self.con.commit()
        return "Successfully card added!"

    @classmethod
    def login(cls, con: sqlite3.Connection, password: str, email: str):
        """
        Login user into shop.
        """
        # Empty message if values are empty
        if not (isinstance(con, sqlite3.Connection) and password and email):
            return "Empty values were given."

        # Hash password into 256 algorithm
        hashed_password = make_password(password)
        # Create cursor from self.con - sqlite3.Connection()
        cursor = con.cursor()

        # Getting user by email and password (hashed)
        user = get_user(cursor, email, hashed_password)
        # Raise AuthRequired exception if user does not exist
        if user is None:
            raise AuthRequired

        # Determine first_name and last_name from user response
        first_name, last_name = user[1:3]

        return cls(con, first_name, last_name, hashed_password, email)

    @classmethod
    def register(
        cls,
        con: sqlite3.Connection,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
    ):
        """
        Registers user into shop.
        """
        # Empty message if values are empty
        if not (
            isinstance(con, sqlite3.Connection)
            and first_name
            and last_name
            and email
            and password
        ):
            return "Empty values were given."

        # Create cursor object from self.con - sqlite3.Connection()
        cursor = con.cursor()
        # Hash password into 256 algorithm
        hashed_password = make_password(password)

        # Request for identical email and first_name, last_name
        if cursor.execute(
            """
            SELECT email FROM user 
            WHERE email = ? or (first_name = ? and last_name = ?)
            """,
            (email, first_name, last_name),
        ).fetchall():
            return "User with this email or name already exists!"

        # Checking for matches email and password
        elif re.match(EMAIL_PATTERN, email) and re.match(PASSWORD_PATTERN, password):
            # Inserting user values into database
            cursor.execute(
                """
                INSERT INTO user (first_name, last_name, email, password)
                VALUES
                    (?,?,?,?)
                """,
                (first_name, last_name, email, hashed_password),
            )
            # Save changes
            con.commit()

            return cls(con, first_name, last_name, hashed_password, email)
        # Email warning message
        elif not re.match(EMAIL_PATTERN, email):
            return "Email must contain @ special character."
        # Password warning message
        elif not re.match(PASSWORD_PATTERN, password):
            return "Password must contain at least 8 characters (at least 1 upper case, 1 number)."

    def show_purchases(self) -> pd.DataFrame:
        """
        Displays user's purchases.
        """
        # Create cursor object from self.con - sqlite3.Connection()
        cursor = self.con.cursor()
        # Getting user by email and password
        user_id = get_user(cursor, self.email, self.password)[0]

        # Raise AuthRequired exception if user does not exist
        if not user_id:
            raise AuthRequired

        # Getting DataFrame by requesting SQL statement with pandas.read_sql_query() and join tables
        df = pd.read_sql_query(
            f"""
            SELECT products.name as 'Product', products.description as 'Description',
            products.price as 'Product price', products.color, purchases.product_quantity as 'Product quantity',
            products.created_at as 'Product Issue date', purchases.purchase_date as 'Purchased date' FROM products
            JOIN purchases ON purchases.product_id = products.id WHERE user_id = {user_id}
            """,
            self.con,
        )

        # Empty message if DataFrame is empty
        if df.empty:
            return "Your purchases list empty."

        return df

    def all_products(self):
        """
        Displays every products.
        """
        # Getting DataFrame by requesting SQL statement with read_sql_query()
        answer = pd.read_sql_query(
            """
            SELECT name as 'Product', created_at as 'Issue date', 
                color, quantity, price 
            FROM products
            """,
            self.con,
        )
        return answer

    def purchase(self, product_name, amount):
        """
        Product purchase.
        """
        # Create cursor from self.con - sqlite3.Connection()
        cursor = self.con.cursor()

        # Getting product by product name
        product = cursor.execute(
            """
            SELECT * FROM products
            WHERE name = ?
            """,
            (product_name,),
        ).fetchone()
        # Not found message if product does not exist
        if not product:
            return "Product not found."

        # Getting user by email and password
        user = get_user(cursor, self.email, self.password)
        if user is None:
            return "User not found."
        # If user card values are None
        elif user[-3] is None:
            return "You do not have access to perform this action. Please add your card to purchase."

        try:
            # Checking user available balance and round values to avoid periodic digits
            if float(product[-1]) * float(amount) <= float(user[-1]) and float(
                amount
            ) <= float(product[-4]):
                product_amount = round(float(product[-4]) - float(amount), 2)
                user_balance = round(
                    float(user[-1]) - (float(product[-1]) * float(amount)), 2
                )

                # Completing purchase adding values into database
                cursor.execute(
                    """
                    INSERT INTO purchases (user_id, product_id, purchase_date, product_quantity)
                    VALUES
                        (?,?,?,?)
                    """,
                    (user[0], product[0], datetime.now(), round(float(amount), 2)),
                )
                cursor.execute(
                    """
                    UPDATE user SET card_balance = ?
                    WHERE id = ?
                    """,
                    (user_balance, user[0]),
                )

                cursor.execute(
                    """
                    UPDATE products SET quantity = ?
                    WHERE id = ?
                    """,
                    (product_amount, product[0]),
                )
                # Save changes
                self.con.commit()
                return "Success! Your purchase added. Your balance: %s" % (user_balance)
        except ValueError as error:
            return error

        return "Please, check your balance or enter valid amount of value."

    def manage_account(self):
        """
        User's account options.
        """
        # Creating cursor object from self.con - sqlite3.Connection()
        cursor = self.con.cursor()
        # Getting user by email and password
        user = get_user(cursor, self.email, self.password)
        # Raise AuthRequired exception if user not found
        if user is None:
            raise AuthRequired

        # Check for user card values
        elif user[-3] is None:
            return "You do not have access to perform this action. Please add your card to purchase."

        # Secure card code stars
        card_code_stars = "*" * 4

        message = f"""
            User: {user[1]} {user[2]}
            Email: {user[3]}
            Card code: {user[-3][:4]} {card_code_stars} {card_code_stars} {user[-3][12:]}
            Card expiration date: {user[-2]}
            Balance: ${user[-1]}
        """

        return message

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
