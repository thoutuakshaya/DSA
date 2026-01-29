# Problem Statement
# While developing a calendar app, you notice that some years have an extra day in February. You recall the leap year rule: a year is a leap year if it is divisible by 4, except if it is divisible by 100, unless it is also divisible by 400. To correctly mark these years, you decide to implement this logic and identify leap years.


n=int(input("year="))
if (n%4==0 and n%100!=0) or (n%400==0):
    print(" Leap Year")
else:
    print("Not a Leap Year")
#time complexity O(1)