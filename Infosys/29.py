def balprobability(n,c,m):
    dp=[[0]*c for _ in range(n)]
    s=sum(m[0])
    for i in range(c):
        dp[0][i]=m[0][i]/s
    for i in range(n-1):
        
        for j in range(c):
            prob=dp[i][j]
            si=sum(m[i+1])+1
            for k in range(c):
                r=m[i+1][k]
                if j==k:
                    r+=1
                re=r/si
                dp[i+1][k]+=prob*re
    
    for j in range(c):    
        print(f"{dp[n- 1][j]:.6f}",end=" ")
    

            

if __name__=="__main__":
    number_of_containers=int(input())
    number_of_colors=int(input())
    matrix=[list(map(int,input().split())) for _ in range(number_of_containers)]
    balprobability(number_of_containers,number_of_colors,matrix)
            