def come(arr):
    n=len(arr)
    a=[]
    b=[]
    for i in  range (n):
        if arr[i]%10==0:
            a.append(arr[i])
        else:
            b.append(arr[i])
    return b+a

arr1=[23,34,90,10,45]
print(come(arr1))

#see intialising array and apendoing for i in arr also comes executes
