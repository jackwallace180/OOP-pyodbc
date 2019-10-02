import pyodbc

# pararemeters/variables for the connection
server = 'localhost, 1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

# establish a connection
conn_nwdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password+'')

cursor = conn_nwdb.cursor()
cursor.execute("SELECT * FROM Orders WHERE ShipCity = 'Rio de Janeiro';")


row = cursor.fetchall()

print(len(row))