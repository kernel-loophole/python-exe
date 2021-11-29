from os import error
from stringcolor import *
from genericpath import getsize
import threading
from ftplib import FTP

import socket
var_check=0
host='127.0.1.1'
port=1097
ftp=(host,port)
def service_connection(sock):
    try:
    
        data1=sock.recv(1024)
        print(cs(data1,"green"))
    except:
        print("error")
def send_file(name_of_file,sock_obj):
    try:
        filename=name_of_file
        f = open(filename,'rb')
        l = f.read(1024)
        while (l):
            sock_obj.send(l)
            print('Sent ',repr(l))
            l = f.read(1024)
            f.close()
        print("File will be send safely")
        return
    except:
        print("error while sending the file ")

   
def start_connections(host, port,sock):
    server_addr = (host, port)
    sock=socket.socket()
    sock.connect((host,port))
    print(cs("Press 1 for send simple massage/n","red"))
    print(cs("Press 2 for send a File :","green"))
    print(cs("Press 3 for Exit to server!","orange"))
    user=int(input())
    if user==1:
        try:
            print("enter your massage ==> ")
            choice=input()

        
            sock.sendall(bytes(choice.encode()))
            print(cs("send","red"),"==>",choice)
            retrive=sock.recv(1024).decode('utf-8')
            if retrive is not None:
                print("Recieve ===>",cs(retrive,"green"))
                    # try:

            #     with open('chal.py','wb') as fp:
            #         ftp.retrbinary('RETR README',fp.write)
            #     ftp.quit()
            # except  error as e :
            #     print("error",e)
            
            # if sock.recv(4096).decode('utf-8'):
            #     x=sock.recv(4096)
            #     print(x)
            #     print("hello")
            # else:
            #     return
        except:
            print(cs("error send message","red"))
                                                                    
    elif user==2:
       name_of_file=input("enter the file name==>")
       send_file(name_of_file,sock)
    elif user==3:
        print("exiting the server")
        return
    
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
check_connection=1
    #if check_connection==0:
#new_tread=threading.Thread(target=service_connection)
#new_tread.start()
        
while True:
    a_event=threading.Event()    
    new_tread=threading.Thread(target=start_connections('127.0.1.1',port,sock),args=[a_event])
    new_tread.start()
    
    

    