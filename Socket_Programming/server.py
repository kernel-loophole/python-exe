import threading
import types
from stringcolor import *
import socket
from ftplib import FTP
import selectors
sel = selectors.DefaultSelector()
host="127.0.1.1"
port=1097
ftp=(host,port)
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen()
print(cs('listening on',"blue"), (host, port))
def recive_file(name_of_file,sock_obj):
    try:
        with open(name_of_file,'wb') as f:
            print("file will be opened")
            while True:
                print('receiving data...')
                data = sock_obj.recv(1024)
                if not data:
                    break
                f.writelines(data)
    except:
        print("file get Successfully")
    
    print("Successfully get the file")
    print('connection closed')
    return

def service_connection():
    print("connect")
    conn, addr = lsock.accept()
    print(cs("press 1 for send massage\n 2 for get file \n 3 for exit ","orange"))
    choice=int(input())
    if choice==1:
        try:    
            recv_data = conn.recv(1024).decode('utf-8')        
            print('Recieve===>', cs(recv_data,"red"))
        except:
                print("error in recive")
        try:
            
            x=input(" enter your message")
            conn.sendall(bytes(x.encode()))
            print(cs("data send===>","red"))
        except:
            print("error")
    elif choice==2:
        name_of_file=input("enter the name of file you wanted to put Data")

        recive_file(name_of_file,lsock)
        
def accept_wrapper():
    conn, addr = lsock.accept()  # Should be ready to read
    print('accepted connection from', addr)
    red=conn.recv(1024).decode('utf-8')
    red.decode()

    if red:
        print(cs("Recieve ====>","blue"),red)

    
(clientsocket, address) = lsock.accept()
while True:
    new=threading.Thread(target=service_connection())
    new.start()
    
    
      