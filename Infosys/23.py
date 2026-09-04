#three sum

def ts(arr,n):
    arr.sort()
    ans=[]
    for i in range(n-2):
        if i>0 and arr[i]==arr[i-1]:
            continue
        left=i+1
        right=n-1
        while left<right:
            if arr[left]+arr[right]+arr[i]==0:
                ans.append([arr[left],arr[right],arr[i]])
                left+=1
                right-=1
                while left <right and arr[left]==arr[left-1]:
                    left+=1
                while left<right and arr[right]==arr[right+1]:
                    right-=1
            elif arr[left]+arr[right]+arr[i]<0:
                left+=1
            else:
                right-=1
    return ans if ans else []




if __name__=="__main__":
    arr=list(map(int,input().split()))
    n=len(arr)
    print(ts(arr,n))