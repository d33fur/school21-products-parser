import sqlite3
import json

def openFile(fileName):
    try:
        with open(fileName, "r", encoding='utf-8') as f:
            return json.load(f)
    except:
        print("unknown file name")

conn = sqlite3.connect('test.db')
index = 0
for i in range(0,81):
    data = openFile(f"{i}.json")
    for j in data:
        name = j['name']
        fat = j['foodEnergy']['fat']
        carbohydrates = j['foodEnergy']['carbohydrates']
        calories = j['foodEnergy']['calories']
        proteins = j['foodEnergy']['proteins']
        #conn.execute(f"INSERT INTO PRODUCTS (ID,NAME,PROTEINS,FAT,CARBOHYDRATES,CALORIES) \
        #             VALUES ({index}, {name}, {proteins}, {fat}, {carbohydrates}, {calories})")
        conn = sqlite3.connect('test.db')

        conn.execute('''CREATE TABLE IF NOT EXISTS products
                     (ID INT PRIMARY KEY     NOT NULL,
                     NAME           TEXT    NOT NULL,
                     PROTEINS       FLOAT     NOT NULL,
                     FAT            FLOAT     NOT NULL,
                     CARBOHYDRATES  FLOAT     NOT NULL,
                     CALORIES       FLOAT     NOT NULL);''')

        conn.execute("INSERT INTO products VALUES(?,?,?,?,?,?);", (index, f'{name}', fat, carbohydrates, calories, proteins))
        conn.commit()
        conn.close()
        print(f"СТРОКА НОМЕР {index} ДОБАВЛЕНА")
        index += 1
