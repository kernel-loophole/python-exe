from typing import Counter


def game_of_wise(string):
    string1=list()
    counter=0
    string2=string.split('0')
    string1=string.split('1')
    print(len(string))
    print(string1)
    print(string2)
    string2+=string1
    print(string2)
    for i in string2:
        string2.remove("")
    string2.remove("")
    if len(string)%2==0:
        return True
    else:
        return False
   
    
def ordering(name):
    string=list(name)
    string1=list()
    string.sort()
    temp=''
    sum=0
    for i in range(0,len(string[::])):
        temp=ord(string[i])

        string1.append(temp-96)

    temp1=0
    string2=list()
    for i in range(0,len(string1)):
        tmp=0
        if(i==0):
            tmp=int(string1[i])*1
        else:
            tmp=int(string1[i])*(i+1)
        #print(tmp," ",end='')
        sum=sum+tmp
    return sum
print(ordering("fiazal"))
if game_of_wise("11110011011"):
    print("singh wins")
else:
    print("shahid wins")