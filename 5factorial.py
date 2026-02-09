#While solving combinatorics problems, you need to calculate factorials of 
# numbers. Factorial of a number N is the product of all positive integers
#  less than or equal to N. To automate this, you decide to write a program 
# that calculates factorials either iteratively or recursively.

# n=int(input())
# l=1
# for i in range(1,n+1):
#     l=l*i
# print(l)

n=int(input())
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(n))

#for both time complexity is O(n)
#3-->6
#5-->120