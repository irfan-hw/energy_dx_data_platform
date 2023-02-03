import mysql.connector
from mysql.connector import Error
from lib.logger import Logger
import config.mysql_config as mysql_config

class MySQLConnection:

    def __init__(self):
        self.connection = None
        self.logger = Logger('root')

    def create_db_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host= mysql_config.HOST,
                user= mysql_config.USER,
                passwd= mysql_config.PASSWD,
                database= mysql_config.DATABASE
            )
            # print("MySQL Database connection successful")
            self.logger.info("Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")
            self.logger.error("Database connection failed")
        
        return self.connection
    
    def insert_sql(self,query):
        self.connection.cursor().execute(query)
        self.connection.commit()
    
    def get_sql(self,query):
        cursor = self.connection.cursor(buffered=True)
        cursor.execute(query)
        return (cursor.fetchall())
    
    def close(self):
        if self.connection.is_connected:
            self.connection.close