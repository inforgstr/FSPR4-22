import sqlite3

from utils import AuthRequired, DB_PATH
from store import Store


def main() -> str:
    con = sqlite3.connect(DB_PATH)
    method = input("Enter method (login, register or 'Q' to quit): ")
    try:
        if method.lower() == "login":
            user = Store.login(con, "mysecretPassword10", "myemail@email.com")

        elif method.lower() == "register":
            user = Store.register(
                con, "Alan", "W", "alan.wk@gmail.com", "RandomAlanPassword"
            )

        print(user.manage_account())

    except AuthRequired as error:
        print(error)
    finally:
        con.close()


if __name__ == "__main__":
    main()
