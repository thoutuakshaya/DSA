def arrange(arr,n):
    arr1=[]
    arr2=[]
    for i in arr:
        if i<0:
            arr1.append(i)
        else:
            arr2.append(i)
    arrn=[]
    if len(arr1)!=len(arr2):
        return " "
    for i in range(len(arr1)):
        arrn.append(arr2[i])
        arrn.append(arr1[i])
    return " ".join(str(i) for i in arrn)

if __name__=="__main__":
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    print(arrange(arr,n))