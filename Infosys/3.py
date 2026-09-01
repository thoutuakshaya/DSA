# Question 1 — Easy/Medium: First Unique Character

# Given a string s, return the index of the first non-repeating character. If every character repeats, return -1.

# Examples
# Input:  s = "leetcode"
# Output: 0
# Input:  s = "loveleetcode"
# Output: 2
# Input:  s = "aabb"
# Output: -1
# Constraints
# 1 <= s.length <= 10^5
# s contains lowercase English letters only

# Expected complexity: O(n)
def find(s):
    
    dict={}
    for i in s:
        dict[i]=dict.get(i,0)+1
    
    for i in range(len(s)):
        if dict[s[i]]==1:
            return i
            
    return -1
        
if __name__=="__main__":
    s=str(input())
    print(find(s))