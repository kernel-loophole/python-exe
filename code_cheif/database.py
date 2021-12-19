from stringcolor import*
from progress.bar import Bar
import time
import logging
def defulter():
    string='''
               

               #######       #######        #############
               #######       #######        #############
               #####################             #####          
               #####################             #####
               #######        ######          ############
               #######        ######          ############
               '''
    print(cs(string,"red"))
def bar():
    string="LOADING"
    logging.basicConfig(filename='mylog.log',level=logging.INFO)
    logging.info("starting the code")
    logging.info("ending the code")
    print(cs(string,"green"))
    bar = Bar(fill="%", max=20)
    for i in range(20):
        time.sleep(0.5)
    # Do some work
        bar.next()
    print()
def database_test():
    string="creating  your database"
   
    print(cs(string,"red"))
    print()
    bar = Bar(fill="#", max=100)
    for i in range(100):
        time.sleep(0.1)
    # Do some work
        bar.next()
    print()
def done():
    print(cs("DATA insert succesfully","green"))

defulter()
bar()
                                           