# Your math teacher challenges you to find the sum of the 
# first N natural numbers. You recall the formula: sum = N * (N + 1) / 2.
# Instead of adding them one by one, you decide to write a program that uses
# this formula to quickly compute the sum for any given N.

# n=int(input())
# l=0
# for i in range (1,n+1):
#     l=l+i;
# print(l)
#time complexity:o(n)

n=int(input())
sum=(n*(n+1))/2
print(sum)
#time complexity:o(1)

#second case is more efficient
#3-->6
#5-->5+4+3+2+1=15