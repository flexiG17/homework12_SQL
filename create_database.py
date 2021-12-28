import sqlite3
import pandas as pd
import re


def clean_field(field):
    return re.sub(r'\<[^>]*\>', '', str(field))


# подключаем базу данных, считываем данные с csv таблицы
con = sqlite3.connect('database.sqlite')
df = pd.read_csv("works.csv")
cursor = con.cursor()

# очищаем столбцы skills и otherInfo от ненужного
df.skills = df.skills.apply(clean_field)
df.otherInfo = df.otherInfo.apply(clean_field)