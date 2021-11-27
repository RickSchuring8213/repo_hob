import pyodbc

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=localhost;'
                      'Database=AdventureWorks2019;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT TOP 100 SEL.* FROM HumanResources.Department sel')

for i in cursor:
    print(i)
