# Question 2 — Medium: Longest Consecutive Sequence

# Given an unsorted integer array nums, return the length of the longest consecutive elements sequence.

# Your algorithm must run in O(n) time.

# Examples
# Input: nums = [100, 4, 200, 1, 3, 2]
# Output: 4

# Explanation:
# The longest sequence is [1, 2, 3, 4].
# Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# Output: 9
# Input: nums = []
# Output: 0
def ans(k,n):
    num_set=set(n)
    longest=0
    for num in num_set:
        if num-1 not in num_set:
            current_num=num
            count=1
            while current_num+1 in num_set:
                current_num+=1
                count+=1
            longest=max(count,longest)
        
    return longest

if __name__=="__main__":
    k=int(input())
    n=[]
    for i in range(k):
        n.append(int(input()))
    print(ans(k,n))