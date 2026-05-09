def palindrome(s):
    left,right=0,len(s)-1
    while left<right:
        if  not s[right].isalnum():
            return False
        if not s[left].isalnum():   
            return False
        if s[left]==s[right]:
            left+=1
            right-=1
        else:
            return False
    return True

def count(s):
    s=s.lower()
    v,c,sp=0,0,0
    for i in s:
        if i in "aeiou":
            v+=1
        elif i==" ":
            sp+=1
        else :
            c+=1
    return c,sp,v

def asciii(s1):
    return ord(s1)

def removevowel(s):
    sw=''
    for i in s:
        if i not in "aeiouAEIOU":
            sw+=i
    return sw
def returncharacters(s):
    sr=''
    for i in s:
        if ('a'<=i<='z') or ('A'<=i<='Z'):
            sr+=i
    return sr
def maxoccurance(s):
    s = s.lower()
    arr = [0] * 26
    for i in s:
        if i.isalpha():
            arr[ord(i) - ord('a')] += 1
    m=max(arr)
    return chr(arr.index(m)+ord('a')),m
def reverse(s):
    return s[::-1]
if __name__=="__main__":
    s="hellO@o@Olleh"
    s1='S'
    print(palindrome(s))
    print(count(s))
    print(asciii(s1))
    print(removevowel(s))
    print(returncharacters(s))
    print(reverse(s))
    print(maxoccurance(s))