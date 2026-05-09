def search(ele,arr,n):
    low=0
    high=n-1
    while low<high:
        mid=(low+high)//2
        if ele==arr[mid]:
            return mid+1,"position"
            
        elif ele<arr[mid] :
            high=mid-1
        else:
            low=mid+1
    return False

if __name__=="__main__":
    arr=[2,3,4,5,6,14,43,15,13]
    ele=60
    n=len(arr)
    print(search(ele,arr,n))