# Chapter 1 - Arrays and Strings

# 1.1 Is Unique: Implement an algorithm to determine if a string has all unique 
# characters. What if you cannot use additional data structures?

def is_unique(s):
    d = {}
    for c in s:
        if c in d:
            return False
        else:
            d[c] = 1
    return True

# 1.1 No additional data structures

def is_unique2(s):
    # Check for empty String
    if len(s) == 0:
        return True
    # Sort the string in alphabetical order
    s = ''.join(sorted(s))
    for c in range(0, len(s) - 1):
        # Compare pairs of characters
        if s[c] == s[c + 1]:
            return False
    return True

