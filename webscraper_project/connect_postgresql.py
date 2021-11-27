import psycopg2

conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="Bananax42?")

cursor = conn.cursor()

# https://stackoverflow.com/questions/34484066/create-a-postgres-database-using-python
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cursor.execute('DROP DATABASE rick_db IF EXISTS')
cursor.execute('CREATE DATABASE rick_db;')
cursor.execute('USE DATABASE rick_db;')
cursor.execute('USE DATABASE rick_db;')