import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="webscr_indeed_db",
    user="postgres",
    password="Bananax42?")

cursor = conn.cursor()

# https://stackoverflow.com/questions/34484066/create-a-postgres-database-using-python
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)


cursor.execute('CREATE DATABASE webscr_indeed_db;')
print("OK")

