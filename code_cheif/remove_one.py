from sqlalchemy import true
from stringcolor import *

def remove_one_fn(arr1,arr2):
    try:
        find_max_one=max(arr1)
        find_max_second=max(arr2)
        find_difference=abs(find_max_one-find_max_second)
        print(find_difference)
    except:
        print(cs("ERROR IS FIND WHILE REMOVEABLE ELEMENT","red"))    
if __name__=="__main__":
    arr1=list()
    arr2=[4,8]
    choice=0
    while True:
        print("press x for exit")
        choice=input()
        if choice=='x':
            break
        else:
            try:
                arr1.append(int(input("enter arr1 data")))
            except:
                print("invalid number")
        
    print(arr1,arr2)    
    remove_one_fn(arr1,arr2)
