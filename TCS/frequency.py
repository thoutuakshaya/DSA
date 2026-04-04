class Solution:
    # Function to sort elements of an array by frequency
    def sortByFrequency(self, arr):
        from collections import Counter

        # Count frequencies using Counter
        freq = Counter(arr)

        # Sort the array with custom key:
        # - primary: frequency in descending
        # - secondary: value in ascending
        arr.sort(key=lambda x: (-freq[x], x))
        

        return arr

# Driver code
if __name__ == "__main__":
    obj = Solution()

    arr = [1, 2, 3, 2, 4, 3, 1, 2]
    res = obj.sortByFrequency(arr)

    print(*res)


'''Instead of writing:

def fun(x):
    return x*2

We write:

lambda x: x*2

Why negative frequency?

Because:
Python sorts ascending.



lambda x: (-freq[x],x)

Means:

sort by freq then number









print(*res)

Means:

Remove brackets and print

Example:

res=[2,2,1]

print(res)
→ [2,2,1]

print(*res)
→ 2 2 1'''