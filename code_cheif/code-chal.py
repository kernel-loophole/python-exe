from stringcolor import *
import numpy as np
def min_max():
    array1=np.array([5,1,2,6])
    array2=list()
    array3=list()
    list_color=['b','w','b','w']
    max_number=array1.max()
    counter=0
    check=False
    temp=0
    
    
    for i in range(0,len(array1)):
        temp=0
        if array1[i]==max_number:
            check=True
            array2.append(array1[i])
            continue
        if check:
            counter+=1
        if counter>=1:
            array2.append(array1[i])
            continue
            # temp=array1[counter]
            # array1[counter]=array1[i]
            # array1[1-i]=temp
        else:
            array3.append(array1[i])

       

            # temp=array1[0]
            # array1[0]=max_number
            # array1[abs(i)]=array1[i-1]
            # print(array1[abs(0+i-len(array1))])     
    new_list=list()
    new_list=array2
    array2+=array3
    print(array2)
    print(list_color)
    max_number=max(array2)
    min_color=min(array2)
    for i in range(0,len(array2)):
        if array2[i]==max_number and list_color[i]=='b':
            max_number=array2[i]
        if array2[i]==min_color and list_color[i]=='w':
            min_color=array2[i]
            print("ok")
    print(max_number,min_color)
    print(cs("counter=","red"),max_number-min_color)
min_max()