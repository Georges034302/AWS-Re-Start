import logging

logfile = 'basic.log'

# set how the log text will be formatted in the file
format_style = '%(asctime)s - %(message)s'

# configure the logger
logging.basicConfig(filename=logfile,format=format_style,filemode='w')

logger = logging.getLogger() # get logging object with the above configurations

logger.setLevel(logging.DEBUG) # Set the log level to start with

# Writing logs to the file
logger.debug('This is a debug message')
logger.info('This is an information message')
logger.warning('This is a warning message')
logger.error('This is an error message')

