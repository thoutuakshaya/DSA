def pathdp(k,n,m):
    ans=0
    directions=[(-1,0),(1,0),(0,-1),(0,1)]
    visited=[[[-1,-1]for _ in range(m) ]for _ in range(n)]
    def visit(i,j,dash):
       
        count=1
        if visited[i][j][dash]!=-1:
            return visited[i][j][dash]
        for r,c in directions:
            newr=r+i
            newc=c+j
            if 0<=newr<n and 0<=newc<m and k[newr][newc]>k[i][j]  :
                count=max(count,1+visit(newr,newc,dash))
            
            if dash==0:
                newr=i+2*r
                newc=j+2*c
                if 0<=newr<n and 0<=newc<m and k[newr][newc]>k[i][j]  :
                    count=max(count,1+visit(newr,newc,1))
                    
        visited[i][j][dash]=count
        return count
    for i in range(n):
        for j in range(m):
            ans = max(ans, visit(i, j, 0))

    return ans
if __name__=="__main__":
    n=int(input())
    m=int(input())
    k=[list(map(int,input().split())) for _ in range(n)]
    print(pathdp(k,n,m))             
                            



