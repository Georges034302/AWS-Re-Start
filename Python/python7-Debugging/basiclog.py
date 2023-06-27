import logging

logfile = 'basicdebug.log'
format_style = '%(asctime)s %(message)s'
logging.basicConfig(filename=logfile,format=format_style,filemode='w')

logger = logging.getLogger()    # create a logger object
logger.setLevel(logging.DEBUG)  # set the type of messages to write to file

# write some messages based on the level to the log file
logger.debug("This is a debugger message")
logger.info("This is an Info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")

