import logging
from logging.handlers import TimedRotatingFileHandler
import energy_dx_data_platform.log_config as log_config

def get_filename(filename):
    return filename

class Logger:
    def __init__(self,name):
        
        self.logger = logging.getLogger(name)
        self.logger.handlers.clear()
        self.logger.setLevel(log_config.LEVEL)

        logHandler = TimedRotatingFileHandler('./logs/energy_dx_data_platform.log', when='midnight', interval=1)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logHandler.setFormatter(formatter)
        logHandler.namer = get_filename
        self.logger.addHandler(logHandler)
        
    
    def error(self, message):
        self.logger.error(message)
    
    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)
