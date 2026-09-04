# nums=[1,1,0,1] o/p=3  longest subarray after deleting one

def l(arr):
    ans=0
    count=0
    k=0
    left=0
    for i in range(left,len(arr)):
        if arr[i]=='0':
            count+=1
        while count>1:
            if arr[left]=='0':
                count-=1
            left+=1
        ans=max(ans,i-left)
    return ans
        

if __name__=="__main__":
    arr=list(map(int,input().split()))
    print(l(arr))