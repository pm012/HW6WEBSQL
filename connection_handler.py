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
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance=super(SQLConnector, cls).__new__(cls)
            cls._instance._initialize_connection()
        return cls._instance




    def _initialize_connection(self):
        self.available_types = ['sqlite', 'mariadb']
        self.logger = logger_instance.HWLogging()

        config = configparser.ConfigParser()
        config.read(CONFIG_FILE)
        db_type = config.get('database', 'db_type')

        if db_type.lower() in self.available_types:
            self.db_type = db_type
        else:
            print('Unknown database type. Please, implement additional connection logic')
            self.db_type = None
            self.connection = None  # Initialize connection attribute

        if self.db_type == 'sqlite':
            db_file = config.get('sqlite', 'database_file')
            self.logger.log_info('SQLite connection db is established')
            self.connection = sqlite3.connect(db_file)
        elif self.db_type == 'mariadb':
            host = config.get('mariadb', 'host')
            port = config.getint('mariadb', 'port')
            username = config.get('mariadb', 'username')
            password = config.get('mariadb', 'password')
            db_name = config.get('mariadb', 'db_name')
            self.connection = mysql.connector.connect(
                host=host,
                port=port,
                user=username,
                password=password,
                database=db_name
            )
        else:
            self.logger.log_info(f"Incorrect DB type. Connector for {self.db_type} is not implemented")
            raise NotImplementedError(f"{self.db_type} db connector not implemented.")

    def get_cursor(self):
        return self.connection.cursor()

    def close_connection(self):
        if self.connection:
            self.connection.close()
            self.logger.log_info('Database connection closed.')
        
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





            

        
        

        