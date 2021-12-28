import sqlite3
import pandas as pd

con = sqlite3.connect('database.sqlite')
df = pd.read_csv("works.csv")
cursor = con.cursor()


