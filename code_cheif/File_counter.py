
def fa():
    total=0
    sum=""
    with open ("test.txt",'r+') as f:
        for i in f:
         
            if i.startswith('u'):
                print(i[7:12])
                sum=i[7:11]+sum
    
    print(sum)
fa()
