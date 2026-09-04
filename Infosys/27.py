def find(rang,numsum):
    def countsum(num):
        s=0
        while num: 
            s+=num%10
            num=num//10
        return s
    current,count=-1,0
    for i in range(rang):
        if countsum(i)==numsum:
            current=max(current,i)
            count=1
        
    return current,count
            

if __name__=="__main__":
    k=int(input())
    s=int(input())
    print(find(k,s))




#brute force
# c=0
    # k=[]
    # for i in range(1,rang+1):
    #     string=str(i)
    #     s=0
    #     for j in range(len(string)):
    #         s+=int(string[j])
    #         if s==numsum:
    #             c+=1
    #             k.append(string)   
    # if k :return "".join(i for i in k) , c 
    # else: return 0, -1