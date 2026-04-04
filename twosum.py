arr=[2,72,11,17,15]
target=9
n=len(arr)
    
dict={}
flag=False
for i in range(n):
    rem=target-arr[i]
    if rem in dict:
        print("elements found",rem,arr[i])
        flag=True
    else:
        dict[arr[i]]=i
if not flag:
    print("elements not found")


    

    