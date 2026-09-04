#mAXIMUM AVERAGE SUBARRAY 
def mas(arr,k):
    n=len(arr)
    s=sum(arr[:k])
    ans=s
    for i in range(k,n):
        s+=arr[i]-arr[i-k]
        ans=max(ans,s)
    return ans/2

if __name__=="__main__":
    arr=list(map(int,input().split()))
    k=int(input())
    print(mas(arr,k))