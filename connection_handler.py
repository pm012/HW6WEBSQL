import configparser
from abc import  ABC
import logger_instance
import sqlite3
import mysql.connector
import os

CONFIG_FILE = "config.ini"
class AbstractConnectionHandler(ABC):
    @classmethod
    def get_connection():
        pass

class SQLConnector(AbstractConnectionHandler):
    def __init__(self, db_type='sqlite'):
        self.available_types = ['sqlite', 'mariadb']
        self.logger = logger_instance.HWLogging()

        if db_type.lower() in self.available_types:
            self.db_type = db_type
        else: 
            print('Unknown database type. Please, implement additional connection logic')
            self.db_type = None

    def get_connection(self):
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE)
        if self.db_type == 'sqlite':
            db_file = config.get('sqlite', 'database_file')
            self.logger('SQLite connection db is established')
            return sqlite3.connect(db_file)
        elif self.db_type == 'mariadb':
            host = config.get('mariadb', 'host')
            port = config.getint('mariadb', 'port')
            username = config.get('mariadb', 'username')
            password = config.get('mariadb', 'password')
            db_name = config.get('mariadb', 'db_name')
            connection = mysql.connector.connect(
                host = host,
                port = port,
                user = username,
                password = password,
                database = db_name
            )
            return connection
        else:
            self.logger(f"Incorrect DB type. Connector for {self.db_type} is not implemented")
            raise NotImplementedError(f"{self.db_type} db connector not implemented. Please check if the connector type is defined correctly or implement the connector")
        
    def get_queries(self, db_type='sqlite'):    
        path = ''
        result = {}
        if db_type == 'mariadb':
            path = 'MariaDB'
        elif db_type == 'sqlite':
            path = 'SQLite'
        folder_path = f'./{path}/'
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.sql'):
                key = os.path.splitext(file_name)[0]
                file_path = os.path.join(folder_path, file_name)
                with open(file_path,'r') as file:
                    file_content = file.read()
                    result[key] = file_content
        return result
    



# if __name__ == '__main__':
#     sq = SQLConnector()
#     file_contents= sq.get_queries('sqlite')
#     for key, value in file_contents.items():
#         print(f'{key}: {value}')





            

        
        

        