from pydoc import doc
from sqlalchemy import true
from stringcolor import *
def fac(n):
    
    counter=1
    if n == 0:
        return 0
    else:
        
        for i in range(0,n):
            for j in range(n,0,-1):
                if i*j==n:
                    print(i,j)
                    counter+=1
                else:
                    continue
    print("Total combination are :===>",counter)
if __name__=="__main__":
    fac(int(input("Enter Number")))