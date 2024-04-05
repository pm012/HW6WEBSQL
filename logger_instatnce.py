import logging
import configparser

class HWLogging():
    def __inint__(self, config_file='config.ini'):
        self.config_file = config_file
        


    def get_logger(self):

        config = configparser.ConfigParser()
        
        config.read(self.config_file)
        filename = config.get('logs', 'filename')
        level = config.get('logs', 'level')
        format = config.get('logs', 'format')
        logging.basicConfig(filename=filename, level=level, format=format)
        return logging.getLogger()
