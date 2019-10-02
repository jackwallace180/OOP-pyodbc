# Connecting SQL to python using pyodbc :taco:

this is an example of us connectingto our SQL server, using python and pyodbc

we will look into:
- Cursor
- Rows
- Querying the DB
- Using while loops for efficient data querys
- Transactions

## connection
using pyodbc (added in settings) to link SQL database and python, get the syntax from pyodbc online. can be used for an database and uses the username password server and databse name to connect 

## .cursor
represts a database cursor, used to manage context of a fetch operation.
cursors cannot delete, add, modify etc

## cursor.execute
executes an sql statement and returns the object.

## .fetchall/.fetchone
fetchall() will return all rows of data from your selected table, this isnt normally used as very bad with big tables. fetchone() will select one row of data from the table and then if printed again will be the next row

