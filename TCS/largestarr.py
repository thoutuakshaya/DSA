def largest(arr,n):
    max=arr[0]
    for i in range (1,n):
        if(arr[i]>max):
            max=arr[i]
    return max
if __name__=="__main__":
    arr1=[3,4,5,6,34,2,2445,3]
    n=len(arr1)
    print(largest(arr1,n))

#if __name__=="__main__": this is return for 
# preventing unintended executipn for reuse purpose.
# when import function is used code within thisis skipped.