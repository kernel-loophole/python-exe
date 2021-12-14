![python pratice](Python.jpeg)
# unittest with Python

```python
from logging import raiseExceptions
import unittest
from stringcolor import *
def sum(self):
    return self**2
def test_your_name(self):
    self.x=input("enter your name")
    return self.x
class teststing(unittest.TestCase):
    def setUp(self):
        self.widget = ('The widget')
```
# String Pattern
```python
import  random
def defaulter():
    string=''' 


                 ###    ###   ###              ##
                 ###    ###   ###               ##
                 ##########   ###   %%%%%%%%$$$$$$##
                 ###   ####   ###                ##
                 ###   ####   ###              ##
                                              ## 
                 
            '''
    print(string)
def ran():
    s=['ali','junaid','hamza','Zain','samad']
    s.sort()
    for i in range(0,len(s)):
        print("hello to",s[i].title(),"and you are invited:")
    for i in s:
        if i=='this':
            s.remove(i)
    for item in range(0,len(s)):
        s[item]=s[item].title()
    print(s) ```
    # Socket Programming
    
    ```python
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
        ```

