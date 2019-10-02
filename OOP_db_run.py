from oop_db_connect import *


db_nw = ConnectMSserver('localhost,1433', 'Northwind', 'SA', 'Passw0rd2018')

print(db_nw.cursor.execute("SELECT * FROM Products").fetchone())

print(db_nw.sql_query('SELECT * FROM Products').fetchone())

print(db_nw.sql_query_one('SELECT * FROM Products'))

print(db_nw.print_all_product_records())

print(db_nw.average_product_price_SQL())

print(db_nw.average_product_price_python())