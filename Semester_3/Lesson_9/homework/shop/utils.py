import hashlib
import sqlite3

from pathlib import Path


PASSWORD_PATTERN = r"^(?=.*\d)(?=.*[a-z])(?=.*[a-zA-Z]).{8,}$"
EMAIL_PATTERN = r"^[\w\-\.]+@([\w\-]+\.)+[\w\-]{2,4}$"
CARD_CODE_PATTERN = r"^[\d]{16}$"
EXPIRATION_DATE_PATTERN = r"^[\d]{2}[\/][\d]{2}$"


DB_PATH = Path(__file__).parent / "shop.db"


class AuthRequired(Exception):
    """
    Custom Authentication required exception for users.
    This exception is raised when user is not authenticated to system.
    """

    def __str__(self):
        return "Access denied, user must be authenticated in the system."


def make_password(password: str) -> str:
    """
    Hashes password using sha-256 algorithm.
    """
    hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
    return hashed_password


def get_user(cursor: sqlite3.Cursor, email: str, password: str) -> tuple:
    """
    Gets user by its email and password.
    """
    user = cursor.execute(
        """
        SELECT * FROM user
        WHERE email = ?
        and password = ?
        """,
        (email, password),
    ).fetchone()

    if user:
        return user
