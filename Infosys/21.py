#maximum product subarray
#input 4
#2 -3 4 -5 
#output 120( 2*-3*4*-5)
def mps(arr,n):
    mini=maxi=ans=arr[0]
    for i in range(1,n):
        if abs(arr[i-1])<=abs(arr[i]):
            if arr[i]<0:
                mini,maxi=maxi,mini
            mini=min(arr[i],mini*arr[i])
            maxi=max(arr[i],maxi*arr[i])
        else:
            mini=arr[i]
            maxi=arr[i]
            
        ans=max(mini,maxi)
    return ans
            
    

if __name__=="__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    print(mps(arr,n))
