def returnrank(arr,n):
    arr1=arr.copy()
    arr1.sort()
    dic={}
    rank=1
    for i in arr1:
        if i not in dic:
            dic[i]=rank
            #dic lo key values rendu kalpithe items antar
            #paina dic[i]ante i key annat rank dani value annt
            rank+=1
    return [dic[i] for i in arr]


if __name__=="__main__":
    arr=[2,3,43,4,3,4,25,3]
    n=len(arr)
    print(returnrank(arr,n))