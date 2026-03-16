# n=int(input("enter side one"))
# m=int (input("enter side two"))
# l=(m**2+n**2)**0.5
# print(l)


import math
nums=[]

while len(nums)<2:
    nums+=list(map(int,input("enter numbers").split()))
if len(nums)!=2:
    print("enter valid inputs")
else:
    a,b=nums
    l=math.sqrt(a*a+b*b)
    print(l)
