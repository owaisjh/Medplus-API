import sqlite3

connection = sqlite3.connect('order.db')

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, username text, user_name text, items text, cost int, address text, contact int, paymenttype text, status int)"

cursor.execute(create_table)


connection.commit()

connection.close()