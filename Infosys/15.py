def total(s):
    n=len(s)
    t=c=0
    first=0
    #strings are immutable so 
    # s.lower () soes not work
    # s=s.lower() works 
    # imp
    for i in range(first,len(s)):    
        if s[i]=="R":
            c+=1
            t+=(c*(c+1))/2
        else:
            first+=c
            c=0   
    return t
if __name__=="__main__":
    schedule=str(input().strip())
    print(total(schedule))
        
