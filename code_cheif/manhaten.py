def min_man(S,T):
    
    total=0
    counter=0
    result=list()
    for i in T:
        mini=10**5
        counter=0
        for j in S:
            counter+=1
            total=abs(j[0]-i[0])+abs(j[1]-i[1])
            #print(j[0],"--",i[0],j[1],"--",i[1])
            # print("total",total)
            if total<mini:
                print(j[0],"--",i[0],j[1],"--",i[1])
                print(total)
                mini=total
                
            if counter==len(S):
                result.append(mini)
    return result
        
    """
    min_man [summary]

    [extended_summary]

    Args:
        S ([list of tuples ]): [tuples have pairs like (3,2)]
        T ([list of tuples ]): [tuples]
    """
s=[(0,0),(1,1)]
t=[(0,1),(1,0)]
print(min_man(s,t))

