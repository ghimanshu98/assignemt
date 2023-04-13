"""
Question 1
Write a python code for converting integer values to Indian currency notations, without
using the currency libraries
Example:
input: 504678
output: 5,04,678

"""

def convert(x):
    # 10crore, crore,10lakh,lakh,thou,ten,one
    x = str(x)
    st = x[-1]
    cnt = 0
    for i in range(len(x)-2, -1, -1):
        cnt += 1
        st = x[i]+st
        if cnt == 3:
            st = ','+st
            cnt = 0
        elif cnt == 2:
            st = ','+st
            cnt = 0

    print(st)

convert(504678)