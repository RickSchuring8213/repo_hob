import pyodbc
import pandas as pd
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=localhost;'
                      'Database=AdventureWorks2019;'
                      'Trusted_Connection=yes;')


query = 'SELECT  sel.* FROM HumanResources.Department sel'
result = pd.read_sql(query, con=conn)
print(result)
result2 = result.head()
print(result2)