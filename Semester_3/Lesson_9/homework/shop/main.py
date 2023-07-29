import sqlite3

from utils import AuthRequired, DB_PATH
from store import Store


def main() -> str:
    con = sqlite3.connect(DB_PATH)
    cursor = con.cursor()
    method = input("Enter method (login, register or 'Q' to quit): ")
    try:
        if method.lower() == "login":
            user = Store.login(con, cursor, "mysecretPassword10", "myemail@email.com")

        elif method.lower() == "register":
            user = Store.register(
                con,
                cursor,
                "Dilan",
                "Smith",
                "dilansm@gmail.com",
                "RandomDilanPassword1",
            )

    except AuthRequired as error:
        print(error)
    finally:
        con.commit()
        con.close()


if __name__ == "__main__":
    main()
