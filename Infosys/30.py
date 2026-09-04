def xor(r,n,nums):
    if r==0 and n==1:
        return nums[0]
    m=sum(nums)
    for i in range(1,r):
        s=0
        for j in nums:
            s+=i^j
        m=max(s,m)
    return m


if __name__=="__main__":
    n=int(input("enter numbers count"))
    r=int(input("enter the range between"))
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    print(xor(r,n,arr))