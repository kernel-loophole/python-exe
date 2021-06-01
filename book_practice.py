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
    print(s)
def file(name_of_file):
    name_of_file+='.txt'
    other_file=open('abc.txt','w')
    try:
        with open(name_of_file) as file_obj:
            for item in file_obj:
                other_file.write(item)
    except:
        print(name_of_file+'file does not find by python::')
    for j in range(0,10):
        other_file.write('####\n')
        print('end')
        
        
            

def make(string):
    s_list=list()
    s_list=string.split(' ')
    print(s_list)
    
def fuzzbuzz():
    total=0
    for item in range(1,1000):
        if item%3==0 and item%5==0:
            total=total+item
        elif item%3==0:
            total=total+item
        elif item%5==0:
            total=total+item
        else:
            continue
    print(total)
def dictr():
    user_0 = {
'username': 'efermi',
'first': 'enrico',
'la':'laal'
    }

    user_1 = {
    'username': 'efermi',
    'first': ['item ','item2','item3'],
    'la':'laal'
        }
    users = {
    'aeinstein': {
    'first': 'albert',
    'last': 'einstein',
    'location': 'princeton',
    },
    'mcurie': {
    'first': 'marie',
    'last': 'curie',
    'location': 'paris',
    },
    }
    empty={}
    for item in range(0,3):
        name=input("enter the name:")
        phone=int(input("enter the phone number:"))
        empty[name]=phone

    for item,k in empty.items():
        print(item,k) 
    #arr=[user_0,user_1]
    #for k,i in user_1.items():
     #   print(k,i)
    #for j in arr:
     #   print(j)


    
def palindrome(string):
    reverse=string[::-1]
    if reverse==string:
        print("yes this is :")
    else:
        print('not a plaindrome')
def largest():
    flag=0
    number=0
    for i in range(2,10000000):
        if flag==1:
            break
        for j in range(1,15):
            if i%j!=0:
                break
            if i%j==0 and j+1==15:
                flag=1
                number=i
                break
    print(number)
def sum():
    sq=0
    sq_1=0
    dif=0
    for i in range(0,100):
        sq+=i*i
        for j in range(0,100):
            sq_1+=j
    sq_1=sq_1*sq_1
    dif=sq_1-sq
    print(dif)
def th():
    counter2=0
    counter=0
    for item in range(1,50):
        counter=2
        while counter<item/2:
            if item%counter!=0:
                print(item)
                counter2+=1
                if counter2==13:
                    print(item)
                break
            counter=counter+1
def finder():
    c=1000
    tmp=0
    for item in range(10,1000):
        for j in range(10,1000):
            tmp=(item*item)+(j*j)
            if tmp==c:
                print("the a and b is:")
                print(item,j)
                return
            

        
defaulter()        
s="You’ll often want to run through all entries in a list, performing the same"
#make(s)
s='10001'
bignum ='7316717653133062491'
#dictr()
#fuzzbuzz()    
#palindrome(s)
#largest()
#sum()
#th()
#finder()
file_name=input("enter the file name:")
file(file_name)