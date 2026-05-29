import logging
logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt= '%m/%d/%Y %H:%M:%S'
    
)
import helper

logging.debug("This is a debug message")
logging.info('this is an info essage')
logging.error("this is a error")
logging.warning("thi is a warning messagr")
logging.critical("this a critical message")
