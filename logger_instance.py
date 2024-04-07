import logging
import configparser

class HWLogging():
    def __init__(self, config_file='config.ini'):
        self.config_file = config_file
        self.logger = logging.getLogger()
        


    def setup_logger(self):
        config = configparser.ConfigParser(interpolation=None)        
        config.read(self.config_file)
        filename = config.get('logs', 'filename')
        level = config.get('logs', 'level')
        format = config.get('logs', 'format')
        logging.basicConfig(filename=filename, level=level, format=format)
    
    def log_info(self, message):
        self.setup_logger()
        self.logger.info(message)

