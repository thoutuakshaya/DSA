# Problem Statement
# In a programming contest, you get a question: determine whether a given number is prime.
#  You remember a prime number is a number greater than 1 that has no divisors other than 1
#  and itself. To solve this, you decide to check divisibility from 2 up to the square root 
# of the number. This way, you can quickly find if any divisor exists and decide primality.
# # n=int(input("number="))
# for i in range(2,int(n**0.5)+1):
#     if int(n%i)==0:
#         print("Not Prime")
        
#     else:
#         print("Prime")
#         break
#time complexity O(sqrt(n))
#it incorrectly identifies some non-prime numbers as prime because it prints "Prime" for every non-divisor found in the loop.

n=int(input("number="))
flag=True
if n<2:
    flag=False
else:
    for i in range(2,int(n**0.5)+1):
        if int(n%i)==0:
            flag=False
        else:
            flag=True
if flag:
    print("Prime")
else:
    print("Not Prime")
#time complexity O(sqrt(n))
