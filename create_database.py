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

cursor.execute('INSERT INTO genders(gender)'
               ' SELECT DISTINCT gender'
               ' FROM works '
               ' WHERE gender IS NOT NULL')

cursor.execute('ALTER TABLE works'
               ' ADD COLUMN gender_id INTEGER REFERENCES genders(id)')

cursor.execute('UPDATE works SET gender_id ='
               '(SELECT id FROM genders'
               ' WHERE gender = works.gender)')

cursor.execute('ALTER TABLE works'
               ' DROP COLUMN gender')
con.commit()

cursor.execute('CREATE TABLE education'
               '(id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'level_of_education TEXT)')

cursor.execute('INSERT INTO education(level_of_education)'
               ' SELECT DISTINCT educationType '
               'FROM works'
               ' WHERE educationType IS NOT NULL')

cursor.execute('ALTER TABLE works'
               ' ADD COLUMN education_type_id INTEGER REFERENCES education(id)')

cursor.execute('UPDATE works'
               ' SET education_type_id ='
               ' (SELECT id'
               ' FROM education'
               ' WHERE level_of_education = works.educationType)')

cursor.execute('ALTER TABLE works'
               ' DROP COLUMN educationType')
con.commit()


