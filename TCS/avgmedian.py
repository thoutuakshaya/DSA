def median(arr,n):
    arr.sort()
    if ((n%2)==0):
        print("even numbers so 2 medians")
        median1=(arr[(n//2)-1]+arr[(n//2)])//2
    else:
        k=n//2
        median1=arr[k]
    return median1
        

def average(arr,n):
    s=sum(arr)
    avg=s//n
    return avg

def add(k,arr):
    arr.append(k)
    return arr

if __name__=="__main__":
    arr1=[1,14,5,7,8]
    n1=len(arr1)
    k=int(input("enter a number"))
    print(add(k,arr1))
    print(median(arr1,n1),"median")
    print(average(arr1,n1),"average re")
    