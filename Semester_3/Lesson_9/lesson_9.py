import sqlite3

from pathlib import Path
from pprint import pprint


# path = Path(__file__).parent / "new.db"


# connection = sqlite3.connect(":memory:")
# cursor = connection.cursor()

# cursor.execute(
#     """
#         CREATE TABLE IF NOT EXISTS toys (
#             id integer primary key,
#             name text,
#             price real
#         );
#     """
# )

# new_toys = [
#     (1, 'Shadow', 32),
#     (2, 'Miko', 10),
#     (3, 'Ork', 21),
#     (4, 'Batman', 21),
#     (5, 'Spiderman', 21),
# ]

# cursor.executemany(
#     """
#     INSERT INTO toys
#     VALUES
#         (?,?,?);
#     """,
#     new_toys
# )


# pprint(cursor.execute("SELECT * from toys;").fetchone())
# pprint(cursor.execute("SELECT name, price from toys;").fetchall())
# pprint(cursor.execute("SELECT * from toys;").fetchmany(3))

# for row in cursor.execute("SELECT * from toys;"):
#     pprint("row: ", row)



# connection.commit()
# connection.close()

# Task
"""
1. Вывести первую строку booking_summary
2. Вывести первые 10 строк booking_summary
3. Сохранить все значения из таблицы, где country равен BRA и сохранить в переменную bra
4. создать такую же таблицу как и в hotel_booking под названием bra_cutomers
5. Записать данные из bra в новую таблицу
6. Вывести данные из стобца lead_time, где пользователь не отменял резервирование (столбец is_canceled) и найти среднее арифметическое  
7. Вывести данные из стобца lead_time, где пользователь отменял резервирование (столбец is_canceled) и найти среднее арифметическое
8. Вывести данные из стобца special_requests, где пользователь отменял резервирование (столбец is_canceled) и найти сумму
9. Вывести данные из стобца special_requests, где пользователь отменял резервирование (столбец is_canceled) и найти сумму
10. Сохранить изменения и закрыть соединение
"""

db_path = Path(__file__).parent / "hotel_booking.db"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 1
first_row = cursor.execute(
    """
    SELECT * FROM booking_summary
    """
)
# pprint(first_row.fetchone())


# 2
first_ten = cursor.execute(
    """
    SELECT * FROM booking_summary LIMIT 10
    """
)
# pprint(first_ten.fetchall())

# 3 
bra = cursor.execute(
    """
    SELECT * FROM booking_summary WHERE country = 'BRA'
    """
).fetchall()
# pprint(bra)

# 4
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS bra_customers_v2 (
        num integer,
        hotel text,
        is_cancelled  boolean,
        lead_time integer,
        arrival_date_year integer,
        arrival_date_month text,
        arrival_date_of_month integer,
        adults integer,
        children integer,
        country text,
        adr real,
        special_requests integer
    )
    """
)


# 5
# cursor.executemany(
#     """
#     INSERT INTO bra_customers_v2 
#     VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
#     """,
#     bra
# )

# 6
cancelled = cursor.execute(
    """
    SELECT avg(lead_time) FROM booking_summary
    WHERE is_cancelled = 0 
    """
).fetchall()

# 7
not_cancelled = cursor.execute(
    """
    SELECT avg(lead_time) FROM booking_summary
    WHERE is_cancelled = 1
    """
).fetchall()
# pprint(not_cancelled)

# 8
cancelled_sum = cursor.execute(
    """
    SELECT SUM(special_requests) FROM booking_summary
    WHERE is_cancelled = 1
    """
).fetchall()
# pprint(cancelled_sum)


# 9
not_cancelled_sum = cursor.execute(
    """
    SELECT SUM(special_requests) FROM booking_summary
    WHERE is_cancelled = 0
    """
).fetchall()
# pprint(not_cancelled_sum)



# Bonus
"""
## Bonus:
- попробуйте использовать библиотеку pandas для нахождения суммы и средне арифметического значения
"""

import pandas as pd

table = pd.read_sql_query("SELECT * FROM bra_customers_v2", conn)

pprint(table["lead_time"].mean())

conn.commit()
conn.close()
