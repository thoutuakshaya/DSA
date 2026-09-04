def ma(arr,n,y,z):
    # costsingle=int(z)*n
    # arr.sort (reverse=True)
    # cost=arr[0]*int(y)
    # return min(cost,costsingle)
    dp=[0]*(n+1)
    dp1=[0]*(n+1)
    dp[0]=dp1[0]=0
    for i in range(1,n+1):
        dp[i]=min(dp[i-1],dp1[i-1])+y
        dp1[i]=min(dp[i-1]+z*max(0,arr[i]-0),
                   dp[i-1]+z*max(0,arr[i]-arr[i-1]))
    return min(dp[n],dp1[n])
    


if __name__=="__main__":
    n=int(input())
    y=int(input())
    z=int(input())
    arr=[]
    for i in range(n):
        arr.append(input())
    print(ma(arr,n,y,z))