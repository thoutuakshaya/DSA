#[2 3 -1 8 4]
#Equilibrium point is 8 left sum is 4 and right is 4 for 
#for this write code

def equilibrium_point(arr):
    n=len(arr)
    for i in range(n):
        left=0
        for j in range(i):
            left+=arr[j]
        right=0
        for k in range(i+1, n):
            right+=arr[k]
        if left==right:
            return arr[i]
    return -1


if __name__=="__main__":
    arr=[2 ,3 ,-1 ,8 ,4]
    print(equilibrium_point(arr))