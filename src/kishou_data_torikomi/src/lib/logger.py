import logging
from logging.handlers import TimedRotatingFileHandler
import datetime, os
import config.log_config as log_config

def get_filename(filename):
    return filename

class Logger:
    def __init__(self,name):
        # logging.basicConfig(
        #                 filename="./logs/" + datetime.date.today().strftime('%Y-%m-%d') + ".log", 
        #                 format="%(asctime)s %(levelname)s %(name)s %(message)s",
        #                 level=log_config.LEVEL
        #             )
        
        self.logger = logging.getLogger(name)
        self.logger.handlers.clear()
        self.logger.setLevel(log_config.LEVEL)

        logHandler = TimedRotatingFileHandler('./logs/kishou_data_shutoku.log', when='midnight', interval=1)
        # logHandler.suffix = (datetime.datetime.today()).strftime('%Y-%m-%d  %H:%M:%S') + ".log"
        # print(  logHandler.suffix)

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
