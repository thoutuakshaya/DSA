def freq(arr,n):
    k={}
    for i in range(n):
        k[arr[i]]=k.get(arr[i],0)+1
    f,s=0,0
    for l,j in k.items():
        if j==1:
            f+=1
        else:
            s+=1
    ki=[]
    ki.append(s)
    ki.append(f)
    return " ".join(str(i) for i in ki) 

if __name__=="__main__":
    n=int(input())
    # arr=[]
    # for i in range(n):
    #     arr.append(input())
    arr=list(map(int,input().split()))
    print(freq(arr,n))

