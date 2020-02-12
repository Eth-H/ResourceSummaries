import logging


#CREATING A NEW LOGGER OBJECT
logger = logging.getLogger(__name__) #Make a new looger, name if after the module (__main__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(levelname)s:%(name):%(message)s")
file_handler = logging.FileHandler("employee.log") #Set file to be logged too.
file_handler.setLevel(logging.ERROR) #Useful if you want different logging levels for certain log files.
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)# Adds above statements to logger.

stream_Handler = logging.StreamHandler() #Creates a new handler to print to console
stream_Handler.setFormatter(formatter)
logger.addHandler(stream_Handler)

a= 10
b = 5
c = 0
def Add_stuff(m,n):
    return m+n
def Subtract_stuff(m,n):
    return m-n
def  Times_stuff(m,n):
    return m*n
def Divide_stuff(m,n):
    try:
        result = m/n
    except: ZeroDivisionError:\
        logger.execution("Tried to divide by zero.") #Includes traceback.
    finally:
        print("Whats up, this text is irrelivant but is executed in successful or failed circumstances thanks to the finally satement.")

    return result

Result1 = Add_stuff(a, b)
logger.info("Successful adding operation.")#Operates with logger object.
Result1 = Add_stuff(a, b)
Result1 = Add_stuff(a, b)
Result1 = Add_stuff(a, b)