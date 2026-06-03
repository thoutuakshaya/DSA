#Problem Statement: Given a matrix 
# if an element in the matrix is 0 then 
# you will have to set its entire column
#  and row to 0 and then return the matrix..

#Examples
#Input: matrix=[[1,1,1],[1,0,1],[1,1,1]]
#Output: [[1,0,1],[0,0,0],[1,0,1]]
#Explanation: Since matrix[2][2]=0.Therfore the 2nd column and 2nd row wil be set to 0
def calc(matrix):
    n=len(matrix)
    m=len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                for row in range(m):
                    if matrix[row][j]!=0:
                        matrix[row][j]=-1
                for col in range(n):
                    if matrix[i][col]!=0:
                        matrix[i][col]=-1
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==-1:
                matrix[i][j]=0
    return print(matrix)






def setZeroes(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        row=False
        col=False
        for i in range(m):
            if matrix[i][0]==0:
                col=True
                break
        for j in range(n):
            if matrix[0][j]==0:
                row=True
                break
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0

        if col:
            for i in range(m):
                matrix[i][0]=0    
        if row:
            for j in range(n) :
                matrix[0][j]  =0
        return matrix

if __name__=="__main__":
    matrix=[[1,1,1],[1,0,1],[1,1,1]]
    calc(matrix)
    print(setZeroes(matrix))

#brute force O(m*n*(m+n))


         
