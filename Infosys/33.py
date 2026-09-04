#house robbing leetcode 198
def robbing(nums,n):
    #n=len(nums)
    dp=[0]*(n+1)
    dp[0]=0
    dp[1]=nums[0]
    for i in range(2,n+1):
        dp[i]=max(dp[i-1],dp[i-2]+nums[i-1])

    return dp[n]


if __name__=="__main__":
    #nums=[1,2,3,1]
    n=int(input())
    nums=list(map(int,input().split()))
    print(robbing(nums,n))