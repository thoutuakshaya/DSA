def mergesort(arr):
    if len(arr)<=1:
        return arr,0
    k =len(arr)//2
    arr1=arr[:k]
    arr2=arr[k:]
    arr1,l=mergesort(arr1)
    arr2,r=mergesort(arr2)
    i,j=0,0
    merged,inversion=[],l+r
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<=arr2[j]:
            merged.append(arr1[i])
            i+=1
        else:
            merged.append(arr2[j])
            j+=1
            inversion+=len(arr1)-i
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    return merged,inversion

arr=list(map(int,input().split()))
print(mergesort(arr))




# Problem 4 — Summer Array: Minimum Swaps
# Tier: Easy (Q1) | Marks: 20 | Topic: Greedy / Inversion Count

# Caution

# Online Trap: Most online solutions simulate bubble sort swaps — 
# O
# (
# N
# 2
# )
# . This times out for 
# N
# =
# 10
# 5
# . The correct approach is inversion counting in 
# O
# (
# N
# log
# ⁡
# N
# )
# .

# Problem
# Given an array of 
# N
#  distinct integers, find the minimum number of adjacent swaps required to sort the array in ascending order.

# Sample Input:

# arr = [3, 1, 2]
# Sample Output:

# 2
# Explanation: Swaps: [3,1,2] → [1,3,2] → [1,2,3] = 2 swaps.

# Constraints: 
# 1
# ≤
# N
# ≤
# 10
# 5
# , all elements distinct.

# Key Insight
# The minimum number of adjacent swaps to sort an array = the number of inversions in the array. An inversion is a pair 
# (
# i
# ,
# j
# )
#  where 
# i
# <
# j
#  but 
# a
# r
# r
# [
# i
# ]
# >
# a
# r
# r
# [
# j
# ]
# .

# Count inversions using Merge Sort in 
# O
# (
# N
# log
# ⁡
# N
# )
# .

# Approach
# Use merge sort. During the merge step, whenever an element from the right half is placed before an element from the left half, it contributes (mid - left_ptr + 1) inversions (all remaining left-half elements are larger).

# Complexity: 
# O
# (
# N
# log
# ⁡
# N
# )
#  time, 
# O
# (
# N
# )
#  auxiliary space.

# Python 3