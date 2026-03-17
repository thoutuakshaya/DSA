def reverse(arr,n):
    f=0
    l=n-1
    while f<l:
        arr[f],arr[l]=arr[l],arr[f]
        
        f=f+1
        l-=1
    return arr

if __name__=="__main__":
    arr=[2,3,4,5,6,3]
    n=len(arr)
    print(reverse(arr,n))