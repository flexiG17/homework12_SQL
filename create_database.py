import sqlite3
import pandas as pd
import re


def clean_field(field):
    return re.sub(r'\<[^>]*\>', '', str(field))


def clean_database():
    cursor.execute('DROP TABLE if EXISTS genders')
    cursor.execute('DROP TABLE if EXISTS education')


# подключаем базу данных, считываем данные с csv таблицы
con = sqlite3.connect('database.sqlite')
df = pd.read_csv("works.csv")
cursor = con.cursor()

# очищаем столбцы skills и otherInfo от ненужного
df.skills = df.skills.apply(clean_field)
df.otherInfo = df.otherInfo.apply(clean_field)

# записываем записи, хранящиеся в DataFrame, в базу данных SQL
df.to_sql("works", con, if_exists='append', index=False)
con.commit()

clean_database()

cursor.execute('CREATE TABLE genders'
               '(id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'gender TEXT)')
print("table genders created")

