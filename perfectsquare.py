# n=int(input("enter number"))
# if n<0:
#     print("negetive")
# else:
#     r=int(n**0.5)
#     if r*r == n:
#         print("perfect")
#     else:
#         print("not")



n=str(input())
print(n[::-1]) #slicing
k=[]
for i in range(len(n)-1,-1,-1):
    k.append(n[i])

re="".join(k)
print(re)

rt=''.join(reversed(n))
print(rt)
