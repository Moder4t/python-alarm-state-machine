
import logging 

# Cnfigurateur de Class
class logHistory:

    def __init__(self):

        LOG_LEVEL = logging.ERROR
        LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
        if LOG_LEVEL >= logging.ERROR: 
            logging.basicConfig(filename = "monSysteme.log", level = LOG_LEVEL, format = LOG_FORMAT) 
        else: 
            logging.basicConfig(level = LOG_LEVEL, format = LOG_FORMAT)

    def debug(self, msg):
        logging.debug(msg)
    def error(self, msg):
        logging.error(msg)
    def critical(self, msg):
        logging.critical(msg)