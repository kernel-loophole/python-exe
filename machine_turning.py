from stringcolor import *
head=0
tape=list()
def push_to_tape(string):
    l=[i for i in string]
    tape=l
    return tape


def check_list(tape):
    l1=len(tape)
    if tape[0]==" ":
        return False
    elif tape[0]=="b":
        return False
    elif tape[0]=='c':
        return False
    elif tape[l1-1]!='c':
        return False
    else:
        return True

def states(tape,head,header):
    a_str='''
            (a,a,R)
             ^
             ^
            '''
    b_str='''
            (b,b,R)
             ^
             ^
            '''
    c_str='''
            (c,c,R)
             ^
             ^
            '''
  
    a_counter=0
    b_counter=0
    if tape[head]=='a':
        print(cs(a_str,"green"))
        print("=========> (a,a,R) moving to next state")
        header="a,a,r"
        return 'a'
    elif tape[head]=='b':
        print(cs(b_str,"red"))
        print("=========>(b,b,R) moving to the next state")
        header="b,b,r"
        return 'b'
    elif tape[head]=='c':
        print(cs(c_str,"orange"))
        print(" =========>(c,c,R) moving to next state")
        return 'c'
    
def turing(string):
    stack=list()
    head=''
    a_counter=0
    b_counter=0
    c_counter=0
    stack_counter=0
    tape=push_to_tape(string)
    i=0
    if check_list(tape):
        
        while len(tape)>i:
            l=states(tape,i,head)
            if l=='a':
                stack.append('a')
                a_counter+=1
                stack_counter+=1
            elif l=='b':
                if stack[stack_counter-1]=='a' or stack[stack_counter-1]=='b' :
                    stack.append('b')
                    b_counter+=1
                    stack_counter+=1
                else:
                    print("reject the c most be at the end of string")
                    return False
                    
            elif l=='c':
                stack.append("c")
                c_counter+=1

            i+=1
        if a_counter==b_counter and c_counter>=1:
            return True



    else:
       
        return False
    
    # print(a_counter)
    # print(b_counter)
    # print(c_counter)
    # print(stack_counter)
def accept_state(string):
    final_check=turing(string)
    accept_str='''
                 ACCEPTED
            ############################
            ############################
            # The STRING is accept###### 
            ############################ '''
    reject_str='''
                 REJECTED
            ###########################
            ###########################
            # The STRING is Rejected#### 
            ############################ '''
    if final_check:
        print(cs("======> (Δ,Δ,R)----->Final state","DarkRed2"))
        print(cs(accept_str,"yellow").bold())
    else:
        print(cs(reject_str,"yellow").bold())
        
if __name__=="__main__":
    
    print(cs("     ENTER THE STRING   ","DarkRed2").bold())
    
    string =input()
    print("============")
    print(cs("TAPE","Maroon").bold())
    print("=============")
    l=[i for i in string]
    print(cs(l,"DarkRed2").bold())
    print("#########")
    accept_state(string)