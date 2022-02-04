from stringcolor import *
from types import coroutine
import numpy
def maxcount(arr):
    count=0
    check_list=dict()
    second_count=0
    
    print(arr)
    for i in range(0,len(arr)):
       for j in range(0,len(arr)):
            if arr[j]==arr[i]:
                
                count+=1
            if j+1==len(arr):
                check_list.update({arr[i]:count})
                count=0
                # if count>second_count:
                #     second_count=count
                #     print(second_count)
            
    print(cs(check_list,"Red"))
    second_count=max(check_list.values())
    for v,k in check_list.items():
        if k==second_count:
            print(v,k)
    
        
if __name__=="__main__":
    arr=numpy.array([1,2,2,3,4])
    maxcount(arr)
            
    