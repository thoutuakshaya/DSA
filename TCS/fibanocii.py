n=input("enter a number count").split()
if len(n)==1 and n[0].isdigit():
    n=int(n[0])
    sn=1
    fn=0
    for i in range (1,n+1):  
        sum=sn+fn #1
        fn,sn=sn,sum
        print(fn)
else:
    print("enter valid sigle digit number")
    

#it ensures that only numbers are entered and only sigle digit numbers
#fails for cases where alphabets are entered or list is entered
#Time complexity is O(N)

#we can still optimise this by fast doubling method that uses mathematical 
#formulae and reduces time completxity to O(log N)


    