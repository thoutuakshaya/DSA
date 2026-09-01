# Problem: Frequency Sort

# Given an array of integers, sort the elements by frequency of occurrence in decreasing order. If two elements have the same frequency, they should appear in the order of their first occurrence in the original array.

# Input:

# n = 8
# arr = [4, 6, 2, 2, 6, 4, 4, 6]

# Output:

# 4 4 4 6 6 6 2 2

# Constraints:

# 1 ≤ n ≤ 10^5
# -10^9 ≤ arr[i] ≤ 10^9

# Requirements:

# Write a complete working program (any language you're comfortable with — Java is fine given your prep material, but use what you'd use in the actual exam).
# State the time and space complexity of your solution.
# Handle the edge case of an empty array or all-unique elements.


def freq(arr,n):
    k={}
    if not arr:
        return ""
    for i in arr:
        k[i]=k.get(i,0)+1
    arr1=[]
    times=0
    for i,j in sorted(k.items(),key=lambda x:x[1],reverse=True):
        
        for l in range(j):
            arr1.append(i)

    return " ".join(str(i) for i in arr1)

if __name__ =="__main__":
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    print(freq(arr,n))