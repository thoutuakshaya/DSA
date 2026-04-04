#find whether given elements in arr1 is arr2
def binarysearch(ele,arr,len):
    
    first=0
    last=len-1
    while first<=last:
        mid=(first+last)//2
    
        if ele==arr[mid]:
            return True
        elif ele<arr[mid] :
            last=mid-1
        else :
            first=mid+1
        
    return False
    
def isSubset(arr1,arr2,m,n):
    if m<n:
        return False
    else:
        arr2.sort()
        for i in range(n):
            Find=binarysearch(arr1[i],arr2,m)
            if not Find:
                return False
            
    return True

if __name__=="__main__":
    arr1=[8,2,3,4,5]
    arr2=[3,4,6,3,2,9,7,5,8]
    n=len(arr1)
    m=len(arr2)
    print(isSubset(arr1,arr2,m,n))
    #print(arr1.issubset(arr2)) for set not list 
    
'''

from collections import Counter

def isSubset(arr1,arr2):
    c1=Counter(arr1)
    c2=Counter(arr2)
    for i in c1:
        if c1[i]>c2[i]:
            return False
    return True
if __name__=="__main__":
    arr1=[11,1,13,21,3,7]
    arr2=[11,3,7,1,13,21,1,1]
    print(isSubset(arr1,arr2))/*
'''