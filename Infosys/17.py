def mergei(intervals,n):
    if not intervals :
        return []
    intervals.sort()
    first=intervals[0]
    result=[first]
    for i in intervals[1:]:
        if i[0]<=result[-1][1]:
            result[-1][1]=max(i[1],result[-1][1])
        else:
            result.append(i)
    return result
if __name__=="__main__":
    n=int(input())
    intervals=[]
    for i in range(n):
        a,b=map(int,input().split())
        intervals.append([a,b])
    print(mergei(intervals,n))