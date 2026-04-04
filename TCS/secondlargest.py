def secLargest(arr,n):
    
    if n<2:
        return -1
    onel=float('-inf')
    temp=float('-inf')
    
    for i in range(n):
        
        if(arr[i]>onel):
            
            temp=onel
            onel=arr[i]
        elif(arr[i]>temp and arr[i]!=onel):
            temp=arr[i]
    if temp==float('-inf'):
        return -1
    return  temp
            

def secSmallest(arr,n):
    if n<2:
        return -1
    ones=float('inf')
    temp=float('inf')
    for i in range(n):
        
        if(arr[i]<ones):
            
            temp=ones
            ones=arr[i]
        elif(arr[i]<temp and arr[i]!=ones):
            temp=arr[i]
    return -1 if temp==float('inf')else temp
        
    

if __name__=="__main__":
    arr1=[6,6,6,62,4,6,7,2,4,6]
    n=len(arr1)
    l1=secLargest(arr1,n)
    s1=secSmallest(arr1,n)
    print(l1,s1)








