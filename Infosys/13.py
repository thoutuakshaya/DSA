def base(n,b):
    a=[]
    while n:
        a.append(n%b)
        n=n//b
    return len(set(a))==1

def find(N):
    import math
    for b in range(2,int(math.isqrt(N))+2):
        if base(N,b):
            return b
    return N-1

N=int(input())
print(find(N))



# ## Infosys SP/DSP Coding Problem — Minimum Base with Identical Digits

# Given a positive integer `N`, find the **smallest base `b ≥ 2`** such that the representation of `N` in base `b` consists of **all identical digits**.

# ### Example

# **Input:**

# ```text
# N = 13
# ```

# **Output:**

# ```text
# 3
# ```

# **Explanation:**

# `13` in base `3` is:

# ```text
# 111
# ```

# because:

# ```text
# 1 × 3² + 1 × 3¹ + 1 × 3⁰
# = 9 + 3 + 1
# = 13
# ```

# So the answer is `3`.

# ### Another important observation

# For any `N > 1`, base `N - 1` always works because:

# ```text
# 11 (base N-1)
# = 1 × (N-1) + 1
# = N
# ```

# Therefore, the answer is always at most `N - 1`.

# ### Constraints

# ```text
# 2 ≤ N ≤ 10^18
# ```

# ### Task

# Explain:

# 1. What a number base means.
# 2. How to convert decimal `N` into another base.
# 3. How to check whether all digits in that representation are identical.
# 4. Why base `N - 1` always works.
# 5. Why a `√N` condition/bound can be useful.
# 6. Give an efficient Python solution suitable for an Infosys SP/DSP coding round.
# 7. Explain the code line by line for a beginner.
