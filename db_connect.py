# int his file we'll make our connection
import pyodbc

# pararemeters/variables for the connection
server = 'localhost, 1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

# establish a connection
conn_nwdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password+'')

print(conn_nwdb)

#create a cursor
#allows us to execute readonly queries on the database
cursor = conn_nwdb.cursor()
#using .execute() on a cursor
cursor.execute('SELECT * FROM Customers;')
print(cursor)

#fetching rows from a cursor - fetch row one
row = cursor.fetchone()

print(row)

#fetch all
# this is bad, we dont use this
rows = cursor.execute("SELECT * FROM Customers;").fetchall()
# print(rows)

#fetch some data using for loop

rows = cursor.execute("SELECT * FROM Products").fetchall()

# for record in rows:
 #   print(record.UnitPrice) #we can access a column of a specific column

#however this is dangerous as we said. as we can clog our machine with too much data
#we can use while loops to be more efficient

rows = cursor.execute("SELECT * FROM Products;")

while True:
    record = rows.fetchone()
    if record is None:
        break
    print(record.UnitPrice)

