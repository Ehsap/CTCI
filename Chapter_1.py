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

# 1.3 URLify: Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold the 
# additional characters, and that you are given the "true" length of the string. 
# (Note: if implementing in Java, please use a character array so that you can perform
# this operation in place.)

# EXAMPLE 
# Input:  "Mr John Smith      ", 13
# Output: "Mr%20John%20Smith"

def urlify(s, s_length):
    # Empty string
    if s_length == 0:
        return s
    return s.replace(" ", "%20")

# 1.4 Palindrome Permutation: Given a string, write a function to check if it is a 
# permutation of a palindrome. A palindrome is a word or phrase that is the same 
# forwards and backwards. A permutation is a rearrangement of letters. 
# The palindrome does not need to be limited to just dictionary words.

# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco cta", etc)

def perm_palindrome(s):
    if len(s) == 0:
        return True
    
    s = s.replace(" ", "")
    s = s.lower()
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    # Check if there is a maximum of 1 odd character count in d
    count_odd = 0
    count_even = 0
    for key, value in d.iteritems():
        if value % 2 != 0: # odd
            count_odd += 1
        else:
            count_even += 1
        if count_odd > 1:
            print(count_odd, count_even)
            return False
    return True 

# One Away: There are three types of edits that can be performed on strings: 
# insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit 
# (or zero edits) away.

# EXAMPLE
# pale,  ple  -> true
# pales, pale -> true
# pale,  bale -> true
# pale,  bae  -> true


    


