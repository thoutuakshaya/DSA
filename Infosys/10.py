def monotonic(arr):
    stack=[]
    k=[-1]*(len(arr))
    for i in range(len(arr)):
        while stack and arr[i]>arr[stack[-1]]:
            l=stack.pop()
            k[l]=arr[i]
        stack.append(i)
    return k
    
            


if __name__=="__main__":
    arr=[4,5,2,10,8]
    print(monotonic(arr))