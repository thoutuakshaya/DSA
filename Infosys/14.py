def defeat(heroes,monster):
    heroes.sort()
    monster.sort()
    i=j=0
    count=0
    
    
    while j<len(monster) and i< len(heroes):
       
        if heroes[i]>=monster[j]:
            count+=1
            i+=1;j+=1
        else:
            i+=1
    return count

heroes=list(map(int,input().split()))
monsters=list(map(int,input().split()))
print(defeat(heroes,monsters))
        
        