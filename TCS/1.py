v=int(input())
w=int(input())
if ((w%2)!=0 or w<(2*v )or w>(4*v)):
    print(-1)
else:
    b=(w-2*v)//2
    a=v-b
    print(a)
    print(b)

#a+b=v ,a*2+b*4=w
#2b=w-2v
#b=w/2 -v
#a=w/2
#// floor division
#/normal division
#%remainder