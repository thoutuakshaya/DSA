# n1=str(input())
# n2=str(input())
# n1=n1.lower()
# n2=n2.lower()



# if sorted(n1)==sorted(n2 ):
#     print("yes")
# else:
#     print("no")
dicto={"name":"akshaya","age":56}
print (*(key for key in dicto.keys()))
print(dicto.keys())
for key,value in dicto.items():
    print(f"{key}:{value}")