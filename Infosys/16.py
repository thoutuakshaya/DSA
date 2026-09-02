def flips(s):
    o=0
    se=0
    for i in range(len(s)):
        r1='0' if i%2 ==0 else '1'
        r2='1' if i%2==0 else '0'
        if s[i]!=r1:
            o+=1
        if s[i]!=r2:
            se+=1
    return min(o,se)
if __name__=="__main__":
    s=input().strip()
    print(flips(s))