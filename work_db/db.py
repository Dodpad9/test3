import sqlite3

connect = sqlite3.connect("../shop.db")
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50),
        price INTEGER,
        count INTEGER 
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50),
        email VARCHAR(100),
        password VARCHAR(50)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS information(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        gender VARCHAR(50),
        email VARCHAR(100),
        password VARCHAR(50)
    )
""")

# with open('work_db\\script.sql', 'r') as f:
#     cursor.executescript(f.read())

with open('work_db\\script.sql', 'r') as f:
    cursor.executescript(f.read())

product_list = [
    # ['Samsung Galaxy S90', 300, 100],
    # ['Lenovo R34', 200, 15]
]

information_list = [
    ['man', 'vdhvd@gmail.com', 'yfh4836'],
    ['woman', 'sijcjd@gmail.com', 'vdjlvlhsvd']
]

# product2 = ['MacBookPro17', 3245, 20]
cursor.executemany("INSERT INTO products(name, price, count) VALUES (?, ?, ?)", product_list)
connect.commit()

cursor.executemany("INSERT INTO information(gender, email, password) VALUES (?, ?, ?)", information_list)
connect.commit()

# cursor.execute("INSERT INTO products(name, price, count) VALUES ('iphone 16', 1200, 50)")
# connect.commit()

# cursor.execute("INSERT INTO users(name, email, password) VALUES ('Ігнат', 'hkdsvdjsd' , 'hchjc')")
# connect.commit()
#
# cursor.execute("INSERT INTO users(name, email, password) VALUES ('Cserd', 'money' , 'bolb')")
# connect.commit()
#
# cursor.execute("INSERT INTO users(name, email, password) VALUES ('Марія', 'cursach45609' , 'hf12_56fhf')")
# connect.commit()

# cursor.execute("INSERT INTO users(name, email, password) VALUES ('Kolya', 'est_hochy' , 'maaaaaaa3253')")
# connect.commit()
#
# cursor.execute("INSERT INTO users(name, email, password) VALUES ('Хліб без хліба', 'hlidbloveyra' , 'hlebuchek34576biliy')")
# connect.commit()



# cursor.execute("SELECT * FROM users")
# users = cursor.fetchall()
# print(users)
# cursor.execute("SELECT * FROM products")
# products = cursor.fetchall()
# print(products)
# cursor.execute("SELECT * FROM categories")
# categories = cursor.fetchall()
# print(categories)

cursor.execute("SELECT * FROM information")
information = cursor.fetchall()
print(information)

cursor.execute("SELECT * FROM users2")
users2 = cursor.fetchall()
print(users2)


categories = cursor.fetchall()
print(categories)

users = cursor.fetchall()
# products = cursor.fetchall()
# print(products)
print(users)
cursor.close()
connect.close()
