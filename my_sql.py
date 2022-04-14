import mysql.connector

class mysql_util:

    def __init__(self,host,user,password,database):
        self.db = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
    
    def create_database(self,database_name):
        cursor = self.db.cursor()
        cursor.execute(f"CREATE DATABASE {database_name}")

    def show_databases(self):
        cursor = self.db.cursor()
        print('List of database names are:')
        cursor.execute("SHOW DATABASES")
        for x in cursor:
            print(x[0])
    
    def show_tables(self):
        cursor = self.db.cursor()
        print("List of table names are:")
        cursor.execute("SHOW TABLES")
        for x in cursor:
            print(x[0])

    def execute_query(self,query):
        cursor = self.db.cursor()
        cursor.execute(query)
        self.db.commit()

"""
mysql_util_obj = mysql_util(host='bjnqjjyrdwceenpesae2-mysql.services.clever-cloud.com', user='ulbbyxidrojqjova', password= 'ZH9q5Hd0m9gBPhAZM7hy', database = 'bjnqjjyrdwceenpesae2')
mysql_util_obj.show_databases()
mysql_util_obj.show_tables()
mysql_util_obj.execute_query('INSERT INTO testtable VALUES(88,888,"no@no.com")')"""