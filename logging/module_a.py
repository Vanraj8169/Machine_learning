import logging

def module_a_function():
    logger = logging.getLogger(__name__)
    logger.debug('This is a debug message from module_a')
    logger.warning("This is a warning message from module_a")
    logger.info("This is an info message from module_a")
    logger.critical("This is a critical message from module_a")
    logger.error('This is an error message from module_a')
