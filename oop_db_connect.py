import pyodbc

class ConnectMSserver():

    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn_db = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+self.password+'')
        self.cursor = self.conn_db.cursor()

    def __filter_query(self, query):
            #doing filtering for said querys
        return self.cursor.execute(query)

    def sql_query(self, squery):
        return self.__filter_query(squery)

    def sql_query_one(self, squery):
        return self.__filter_query(squery).fetchone()

    def print_all_product_records(self):
        query_rows = self.__filter_query("SELECT * FROM Products;")
        while True:
            record = query_rows.fetchone()
            if record is None:
                break
            print(record)

    def print_all_records_from_table(self, table):
        query_rows = self.__filter_query(f"SELECT * FROM {table}")
        while True:
            record = query_rows.fetchone()
            if record is None:
                break
            print(record)

    def average_product_price_SQL(self):
        query_rows = self.__filter_query("SELECT AVG(UnitPrice) FROM Products;").fetchall()
        return query_rows

    def average_product_price_python(self):
        query_rows = self.__filter_query("SELECT * FROM Products")
        prices=[]

        while True:
            record = query_rows.fetchone()
            if record is None:
                break
            prices.append(record.UnitPrice)
        return (sum(prices)/len(prices))










#CRUD

#create an entry
    #use insert
    #the cursor cannot make transactions (go to documentation)
#read all entry
    #fetch all record and return as a list of dictionarys
#read 1 entry
    #fetch a specific record
    #get one value using ID

#update 1 entry
    #the id of the record to update
    #update the specific table
    #Update table
#destroy 1 entry
    #the id of the sepecific record
    #destroy the record




