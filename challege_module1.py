
from stringcolor import *
import os,re
def paris(x):
    emptylist=list()
    make_list=list()
    distance=0
    distance2=0
    x=int(x)
    count=0
    test=list()
    for i in range(1,x):
        make_list.append(i)
        test.append(0)

    print(test)
    print(make_list)

    for j in range(0,len(make_list)):
        for m in range(0,len(make_list)):
            for k in range(0,len(make_list)):
                distance=abs(make_list[j]-make_list[j])+abs(make_list[j]-make_list[k])
                if distance  in make_list:
                    test[m]+=1
                    print("[{},{}]".format(make_list[j],make_list[k]))
                    count+=1
            

            print(make_list[j],make_list[k])
    print(test)
def unpreditable(array1,updatees):
    damy=list()
    num=0
    looper=len(array1)-1
    print(array1[len(array1)-1])
    for i in range(0,looper):
        print(array1[i])
        print("i===",i)
        damy.append(abs(array1[i]-array1[i+1]))
    for j in range(0,len(damy)):
        for k,l in updatees.items():
            print(updatees.values())
            if damy[j]==updatees[k]:
                print("match")
                num=updatees.values()
                damy[j]=updatees[k]
    #damy.append(abs(array1[len(array1)-2]-array1[len(array1)-1]))
    print(damy)



def transection(num):
    withdraw=int(input("enter the amount to withdraw"))
    if num<withdraw:
        return False
    if withdraw%5==0:
        print("transection is succeeful ")
        num=num-withdraw-0.5
        print("remaining balance is:",num)
def dic():
    x=dict()
    for i in range(0,5):
        x[i]=i*i*i
    for j,k in x.items():
        print("j ={0} and k={1}".format(j,k))


def sumofnum(num):
    num=str(num)
    if len(num)<2:
        return None
    else:
        num1=int(num[len(num)-1])
        num2=int(num[0])
        return num1+num2
    print(type(num))
def os_ult():
    cwd=os.getcwd()
    print(cs(cwd,'red'))
def try_and_finall():
    try:
        1/0
    finally:
        try:
            2/0
        finally:
            return 45
def codeland(str):
    if len(str)<4 or len(str)>25:
        return False
    string1=re.compile('[^a-zA-Z0-9_]')
    if string1.match(str[0]) is not None:
        return False
    x=len(str)
    if str[x-1]=='_':
        return False
    else:
        return True



def long_word(str):
    longest=str.split()
    print(cs(longest,"red"))
    return max(longest)
def brack_combination(num):
    if num==0:
        return 0
    if num==1:
        return 0
    return 2**num-num
def sub_string( string=["aaabaaddae","aed"]):
    string_1=string[0]
    substring=string[1]
    result=''
    counter=1
    total=list()
    mini=len(string_1)
    looper=0




    for i in range(0,len(string_1)-2):
        result=''
        #if counter==len(substring):
          #  if result!='' or result!=None:
           #     total[looper]=total.append(result)
        for k in range(i,len(string_1)):
            result=result+string_1[k]
        counter=0
        if result!=None:
            total[looper]=total.append(result)
        for j in range(0,len(substring)):
            if substring[j] in result:
                counter=counter+1

    total[0]='amammamamam'
    mini=len(total[0])
    final_str=''
    for i in range(0,len(total)):
        if mini>len(total[i]):
            mini=len(total[i])
            final_str=total[i]


    return final_str
def pos_arg(arg,/):
    print(arg)
def keyword(*,arg):
    print(arg)





def FirstReverse(strParam):
  if len(strParam)==0:
    return strParam
  final_str=strParam[::-1]
  counter=len(strParam)
  for i in range(len(strParam),0):
    print("helo")
    final_str=final_str+strParam[i]

  # code goes here
  return final_str
# keep this function call here 
#print(FirstReverse(('pak')))    
##print(long_word("fun&!! time"))
x=2
#print(pos_arg(x))
#print(keyword(arg=9))
#print(type(x))
#repr(x)
#print(type(x))
y='string'
c=['string',4,'test']
d=['orange',340390,'hjhfj']
#print(cs(d,'red'))
string='u__hello_world123'
#if codeland(string):
 #   print(cs("yes the user name is valid",'orange'))
#else:
 #   print(cs("not valild",'red'))
#test=['test','list','paksi']
#print(test)
#for i in test[:]:
 #   test.remove(i)
#print(test)
#print(try_and_finall())
#os_ult()
#sumofnum(333)
#print(dic())
#transection(300)
array1=[1,2,4,6,8,7]
array2={2:3,4:5}
#unpreditable(array1,array2)
#num=int(input("enter the number of bracket"))
#print(cs("number of combinations are ::-->   ","red"))
#print(brack_combination(num))
paris(4)