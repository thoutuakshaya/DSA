# Problem 1 — Maximum Subarray Sum
# Tier: Easy (Q1) | Marks: 20 | Topic: Arrays

# Problem
# Given an array of integers (which may include negative numbers), find the maximum sum of any contiguous subarray. The subarray must contain at least one element.

# Sample Input:

# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Sample Output:

# 6
# Explanation: Subarray [4, -1, 2, 1] has sum = 6.

# Constraints: 
# 1
# ≤
# N
# ≤
# 10
# 5
# , 
# −
# 10
# 4
# ≤
# a
# r
# r
# [
# i
# ]
# ≤
# 10
# 4
# .

# Key Insight
# Use Kadane's Algorithm: maintain a running sum curr. At each element, either extend the existing subarray or start fresh from the current element. Track the global maximum.

# The decision at each step: curr = max(arr[i], curr + arr[i]).

# Approach
# Initialize curr = arr[0], best = arr[0].
# For each arr[i] from index 1 onward:
# curr = max(arr[i], curr + arr[i]) — extend or restart.
# best = max(best, curr) — update global max.
# Return best.
# Complexity: 
# O
# (
# N
# )
#  time, 
# O
# (
# 1
# )
#  space.

def subarray(arr):
    curr=arr[0]
    best=arr[0]
    for i in arr[1:]:
        curr=max(curr+i,i)
        best=max(best,curr)
     
    return best

if __name__=="__main__":
    arr=[-2 ,1 ,-3 ,4, -1, 2 ,1 ,-5,4 ]
    print(subarray(arr))
