#coin change leetcode

def coin(coins,amount):
    INF=float('inf')
    dp=[INF]*(amount+1)
    dp[0]=0
    for i in range(1,amount+1):
        for c in coins:
            if i>=c:
                dp[i]=min(dp[i],dp[i-c]+1)
            
    return dp[amount]

    


if __name__=="__main__":
    amount=int(input())
    coins=list(map(int,input().split()))
    print(coin(coins,amount))