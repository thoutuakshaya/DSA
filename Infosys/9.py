def non (s):
    k={}
    for i in s:
        k[i]=k.get(i,0)+1
    for i in range(len(s)):
        if k[s[i]]==1:
            return i
    return -1
if __name__=="__main__":
    s="lzzeetlcode"
    print(non(s))