n=str(input())
n=n.lower()
s="aeiou"
c=0
for i in n:
    if i in s:
        c+=1
print(c)