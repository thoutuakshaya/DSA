#to find smallest in array
def smallest(arr,n):
    min=arr[0]
    for i in range(1,n):
        
        if(arr[i]<min):
            min=arr[i]
    return min

arr1=[2,3,4,6,1,0,-1]
n=len(arr1)
s=smallest(arr1,n)
print(s)
