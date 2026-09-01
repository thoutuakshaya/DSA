def find(s):
    k={}
    start=0
    l=0
    m=0
    for i in range(start,len(s)):
        k[s[i]]=k.get(s[i],0)+1
        if k[s[i]]==1:
            l+=1
            m=max(l,m)
        else:
            while k[s[i]]==1:
                k[s[i]]-=1
                start+=1
    return m





if __name__=="__main__":
    s=str(input())
    print(find(s))