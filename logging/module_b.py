import logging

def module_b_function():
    logger = logging.getLogger(__name__)
    logger.debug('This is a debug message from module_b')
    logger.warning("This is a warning message from module_b")
    logger.info("This is an info message from module_b")
    logger.critical("This is a critical message from module_b")
    logger.error('This is an error message from module_b')
