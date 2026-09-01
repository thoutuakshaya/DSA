def rotate(arr,k):
    n=len(arr)
    k%=n
    if k==0:
        return arr
    def reverse(a):
        l=0
        r=len(a)-1
        while l<r:
            a[l],a[r]=a[r],a[l]
            l+=1;r-=1
    reverse(arr)
    reverse(arr[:k])
    reverse(arr[k:])
    return arr

if __name__=="__main__":
    arr=list(map(int,input().split()))
    k=int(input())
    print(rotate(arr,k))