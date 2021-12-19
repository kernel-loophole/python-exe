import numpy as np
def pramid(starting ,ending):
    counter=0
    pramid_data=[[1],[2,3],[4,5,6],[7,8,9,10]]
    print(pramid_data)
    for i in pramid_data:
        if i[0]==starting:
           
            for j in i:
                if ending==j:
                    print(j)
    """
           1
          2 3
         4 5 6
        7 8 9 10
    pramid [summary]

    [extended_summary]

    Args:
        starting ([type]): [description]
        ending ([type]): [description]
    """
pramid(1,2)