import argparse
from stringcolor import *
preser=argparse.ArgumentParser()
print(cs("   arguments","red"))
preser.add_argument("-t",'--test',help="this is help")#postional arguments
preser.add_argument("-v","--verbosity",choices=[0,1,2],type=int)#optional arguments
arg=preser.parse_args()
print(cs("HERE IS ARGUMENTS++","blue"))
print(cs(arg.test,"green"))

if arg.verbosity==0:
    abc=int(input("enter your name"))
    if abc==0:
        print("welcome")
    else:
        ("hi")

    print("your key  ")
    print(cs("this is 0","red"))
elif arg.verbosity==1:
    print(cs("this is 1","orange"))
else:
    print("NOT COLORING")
