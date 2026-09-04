def basecheck1 (num,k):
    rem=num%k
    num=num//k
    while num>=k and (rem==num%k):
        num=num//k
    if num==rem:
        return True
    return False


num=int(input())
k=2
while not basecheck1(num,k):
       k=k+1
print(k)
    