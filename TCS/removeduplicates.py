def removeDuplicates(arr,n):
    i=0
    arr.sort()
    print(arr)
    for j in range(1,n-1):
        if arr[i]==arr[j]:
            continue
        else:
            i=i+1
            arr[i]=arr[j]
    return i+1



if __name__=="__main__":
    arr1=[1,1,7,9,2,2,4,5,2,3,3,3,4,4,5,7,9]
    n1=len(arr1)
    res=removeDuplicates(arr1,n1)
    print(arr1[:res])
