from os import stat
from typing import Counter, final
import json
from progress.bar import Bar
import logging
import time
from stringcolor import *  # form coloring the text
def bar():
    string="LOADING please wait"
    logging.basicConfig(filename='mylog.log',level=logging.INFO)
    logging.info("starting the code")
    logging.info("ending the code")
    print(cs(string,"green"))
    bar = Bar(fill="#", max=10)
    for i in range(10):
        time.sleep(0.2)
    # Do some work
        bar.next()
    print()
def add(name,phone_number,counter):
    if counter==0:
        with open ("records.txt","r+") as f:
            f.writelines("names:    phone numbers\n")

   
    with open("records.txt",'r+') as f:

        for i in f:
            f.writelines("{}:  {}\n".format(name,phone_number))
    print(cs("###THE USER ADD SUCCECFULLY####","orange"))
    return
def search(name):
    name+="\n"
    with open("records.txt","r+") as f:
        for v in f:
            p=v
            copystr=v
            test=p.split(" ")
            if name in test:
                print("find")
                print(copystr)
                return
            else:
                continue
        print(cs("not find","yellow"))
def remove(name,counter):#function to remove user 
    plus=0
    name+="\n"
    check=False
    with open("records.txt","r+") as f:
        for v in f:
            start=0
            end=0
            plus+=len(v)
            print(v)
            if v.startswith(name[0]):
                check=True
                print(cs("USER DELETE SUCCESFULLY","yellow"))
                start=abs(len(v)-plus)
                end=plus+len(v)
                counter=counter-1
                break
        if check:
            f.seek(start)
            f.write("                           ")
        else:
            print("the user does not exist")
            
          
def display():#display the data
    with open("records.txt","r") as f:
        for v in f:
            print(cs(v,"cyan"))


Counter=0
while True:
    print(cs("********* FOR  DISPLAY NUMBER OF USER  PRESS 99  ******* ","green"))
    choice=int(input(cs("press \n1>>\n for add user\n  \n2>>\n for Display\n   3>>for Find  \n 4->>\nfor delete\n 0>> for EXIT\n","red")))
    if choice==1:
        bar()
        name=input(cs("enter your name:---->","cyan"))
        number=int(input(cs("enter your phone number---->","blue")))
        add(name,number,Counter)
    elif choice==2:
        bar()
        display()
    elif choice==3:
        name=input("enter name to find")
        search(name)
    elif choice==4:
        name=input("enter the name to delete\n")
        bar()
        remove(name,Counter)
    elif choice==0:
        print("bye bye!!!")
        break
    else:
        ("invalid")