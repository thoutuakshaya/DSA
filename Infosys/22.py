def sort(arr,k):
    # for i in range(len(arr)):
    #     if k-arr[i] in arr:
    #         return [arr[i], k-arr[i]]
    # return -1
    left=0
    right=len(arr)-1
    while left<right:
        if arr[left]+arr[right]==k:
            return [arr[left],arr[right]]
        elif arr[left]+arr[right]<k:
            left+=1
        else:
            right-=1
    return -1
if __name__=="__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    print(sort(arr,n))


# two sum