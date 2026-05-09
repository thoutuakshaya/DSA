class solution:
    def productmax(self,arr, n):
        prefix=1
        suffix=1
        product=float("-inf")
        for i in range(n):
            if prefix==0:
                prefix=1
            if suffix==0:
                suffix=1
            suffix*=arr[n-1-i]
            prefix*=arr[i]
            product=max(product,max(prefix,suffix))
        return product

if __name__=="__main__":
    arr1=[1,14,5 ,-1,0,7,8]
    n1=len(arr1)
    sol=solution()
    print(sol.productmax(arr1,n1))