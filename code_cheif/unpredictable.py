import numpy as np
from stringcolor import *
def unpred_arr(repalace,arr):
    key=0
    
    new_arr=list()
    empty_list=[]
    counter=0
    value=0
  
    while True:
        for i in new_arr[::]:
            new_arr.pop()
      
        for i in range(0,len(arr)-1):
            sum_arr=0
            x=abs(arr[i]-arr[i+1])
            new_arr.append(x)
            #print(arr[i]-arr[i+1])
        # print(new_arr)
        sum_arr=sum(new_arr)
        print(sum_arr)
        for i,j in repalace.items():
            # print("value of j==.",j)
        
            if j==int(sum_arr):
                value=j
                # print("in the if")
                # print("=====<",i)
                key=i
                break
        key=int(key)
        value=int(value)
        #print("key===>",key,"++++>value",value)
        for l in range(0,len(arr)):
            
            if key==0:
                break
            if arr[l]==int(sum_arr):
                arr[l]=key
                continue
            if arr[l]==key:
                # print("vlaue of arr",arr[l])
                arr[l]=value
            
        # print("=======>",arr)
        if counter==len(repalace):
            break
        else:
            counter+=1
            continue
    print("New Array")
    print(cs(arr,"red"))
    return arr
if __name__=="__main__":
    arr=np.array([3,2,3,4,5])
    d={"1":3,"3":4,"1":5}
    unpred_arr(d,arr)