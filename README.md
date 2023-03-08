![python pratice](Python.jpeg)
# unittest with Python
HI
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
# Pytest
```python
from example_test import add_two
class TestClass:
    def test_task1(x):
        assert add_two(12,12)==24
    def test_tas2():
        assert add_two(0,0)==0
def test_9():
    assert add_two(12,0)==12

def test_check():
    assert add_two(12,12)==24

```
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

# Scrapy
```python
from fileinput import filename
from unicodedata import name
from django import urls
import scrapy
# classes are spider, item, and fields
class Spider(scrapy.Spider):
    #name: identifies the Spider. It must be unique within a project, that is, you can’t set the same name for different
       #Spiders.
    name = "spider"
    def start_requests(self):
    
        start_urls = ['http://quotes.toscrape.com/page/1/',


        'http://kernel-loophole.github.io/This-Is-Hiader/',]
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        page=response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')    
```
# Generator Function
```python
def genator(n):
    for i in range(n):
        if i%2==0:
            yield i
        else:
            continue
def check_gen(gen):
    for i in gen:
        print(i)
check_gen(genator(10))
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
    
```

