# Chapter 1 - Arrays and Strings

# 1.1 Is Unique: Implement an algorithm to determine if a string has all unique 
# characters. What if you cannot use additional data structures?

def is_unique(s):
    """
    Add each character in s into a map. If a key already exists for a
    character you want to add in the array, then the string is not unique.
    """
    d = {}
    for c in s:
        if c in d:
            return False
        else:
            d[c] = 1
    return True

# 1.1 No additional data structures

def is_unique2(s):
    """
    Sort the string and compare each pair of characters. If a pair has
    the same characters, then the string is not unique. 
    """
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

# 1.2 Check Permutation: Given two strings, write a method to decide if one 
# is a permutation of the other.

def is_perm(s1, s2):
    """
    Compare the characters and their counts between s1 and s2. s2 is a perm
    of s2 if and only if the characters and their counts are the same.
    """
    if len(s1) == 0 or len(s2) == 0:
        return False

    if len(s1) != len(s2):
        return False
    d1 = {}
    d2 = {}
    # Add s1 characters and counts to d1
    for c in s1:
        if c in d1:
            d1[c] += 1
        else:
            d1[c] = 0
    # Add s2 characters and counts to d2
    for c in s2:
        if c in d2:
            d2[c] += 1
        else:
            d2[c] = 0
    # Compare d1 and d2
    for key, value in d1.iteritems():
        if key in d2:
            if value != d2[key]:
                return False
        else:
            return False
    return True

