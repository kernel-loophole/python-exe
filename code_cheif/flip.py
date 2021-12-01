from typing import Counter
from stringcolor import *
import re
# function in function 
def abc():
    print("hello abc")
    def xyz():
        print("hello xyz")
    xyz()
def flip_0_1(string):
    test=list()
    test1=""
    check=False
    get=[string for string in re.split(r'(\w{3})',string) if string ]
    # if len(string)>3:
    #     chuck,chuck_size=len(string),len(string)//2
    #     for i in range(0,len(string)):
    #         if check:
    #             test1=""
    #         test1=str(i)+str(test1)
    #         if len(test1)==3:
    #             test.append(test1)
    return get
def brake_it(passed_string):
    Counter=1
    final_list=list()
    x=flip_0_1(passed_string)
    print(x)
    total=0
    for i in x:

        Counter=0
        for j in i:
            if j=="0":
                print("hello")
                Counter=Counter+1
            total+=1
            print(j,end="")
            print("counter",Counter)
            if Counter>1:
                final_list.append("yes")
                break
            if  total==len(i):
                final_list.append("NO")

            
    print(final_list)        
brake_it("000101000010")
# abc()