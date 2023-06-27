import logging

# Create a logger object
logger = logging.getLogger(__name__)

# Set the logging level
logger.setLevel(logging.ERROR)

# Create file handler to write logs to file
file_handler = logging.FileHandler('debugging.log')

# Setup the log messages format
format_style = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')

# Associate the formatting style with the log file
file_handler.setFormatter(format_style)

# Associate the logger with the file handler to write to the log file
logger.addHandler(file_handler)

a = input("a = ")
b = input("b = ")

try:
    a = int(a)
except ValueError:
    logger.error(f'ValueError: {a} should be an integer')
except TypeError:
    logger.exception(f'Cannot cast {a} to int')
    
try:
    b = int(b)
except ValueError:
    logger.error(f'ValueError: {b} should be an integer')
except TypeError:
    logger.exception(f'Cannot cast {b} to int')

try:
    print(a/b)
except ZeroDivisionError:
    logger.error(f'DivisionByZero: b cannot be ZERO')
