def cancel(days,obli,can,arr):
    s=1
    k=0
    length=0
    for i in range(1,days+1):
        if i in arr :
            k+=1
            
        while k>can :
            if s in arr:    
                k-=1
            s+=1
        length=max(length,i-s+1)

    return length

if __name__=="__main__":
    days=int(input())
    obli=int(input())
    can=int(input())
    k=[]
    for _ in range(obli):
        k.append(int(input()))
    k.sort()
    print(cancel(days,obli,can,k))