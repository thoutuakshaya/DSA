def repeated(arr,n):
    dict1={}
    for i in  arr: 
        dict1[i]=dict1.get(i,0)+1
        
    for i,j in dict1.items():
        if j>1:
            print (i,"repeated")
        else:
            print(i,"not repeated")
'''     
from collections import Counter
def repeated(arr):
    countIt=Counter(arr)
     
    for i,j in countIt.items():
        if j>1:
            print(i ,"repeated")
        else :
            print(i,"not repeated")
'''         
if __name__=="__main__":
    arr=[2,3,43,4,3,4,25,3]
    n=len(arr)
    print(repeated (arr,n))