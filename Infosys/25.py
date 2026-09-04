#maximum number of vowels in substing of given length
#s="abciiidef" k=3 o/p =3

def stri(s,k):
    vowels={"e","a","i","o","u"}
    l=s[:k]
    count=0
    for i in range(len(l)):
        if s[i] in vowels:
            count+=1
    first=count
    for i in range(k,len(s)):
        if s[i] in vowels:
            count+=1
        if s[i-k] in vowels:
            count-=1

        first=max(first,count)
    return first

if __name__=="__main__":
    s=str(input())
    k=int(input())
    print(stri(s,k))


