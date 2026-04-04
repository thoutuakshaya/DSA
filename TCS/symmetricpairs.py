def symmetric(arr):
    hi={}
    for first ,second in arr:
        if second in hi and hi[second]==first:
            print("sym found",first,second)
        else:
            hi[first]=second
    
if __name__=="__main__":
    arr=[(1,2),(3,4),(5,6),(2,1),(4,3)]
    symmetric(arr)