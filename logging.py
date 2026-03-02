import logging


logging.basicConfig(level=logging.INFO)
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')
logger = logging.getLogger("mylogger")
logger.setLevel(level=logging.DEBUG)
hander = logging.FileHandler(filename="mylog.log")
formatter = logging.Formatter(
    "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d)] - %(message)s"
    )
hander.setFormatter(formatter)
logger.addHandler(hander)
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')