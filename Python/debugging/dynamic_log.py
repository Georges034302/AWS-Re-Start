import logging

# create a logger object, connect it to the script name
logger = logging.getLogger(__name__) # refers to the root-code triggering the script

# Set the level of logging (errors I want to record)
logger.setLevel(logging.ERROR)

# Create a file handler to write logs
file_handler = logging.FileHandler('debugging.log')

# Set the log format in the file
format_style = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')

# Connecting the file with the format style
file_handler.setFormatter(format_style)

# Add the file_handler to the logger, so the logger can write records
logger.addHandler(file_handler)

a = input('a = ')
b = input('b = ')
try:
    a = int(a)
except ValueError:
    logger.error(f'ValueError: a should be integer')
    
b = int(b)
try:
    print(a/b)
except ZeroDivisionError:
    logger.error(f'b cannot be zero')
