import logging
"""
DEBUG: Detaialed infomation, typically of interest when only diagnosing problems.
INFO: Confirmation that things are working as expected.
Warning: An indication that something unexpected happened, or indicative of soem problem in the near future. Though the software is still working as expected.
ERROR: Due to a more serious problem, the software has not been able to perform some function.
CRITICAL: A serious error, indicating that the program itself may be unable to continue running.
Default level is warning.
root looger used if not specified
"""

logging.basicConfig(filename="test.log",level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s")

#Log to chosen file; Change level to debug so now logging.debug can be used;
# format is to edit format of loggerd statments, see LogRecord attributes.txt;


a = 10
b=5
def Add_stuff(m, n):
    return m+n

Result = Add_stuff(a, b)
logging.info("Add: {} + {} = {}".format(a, b, Result))




