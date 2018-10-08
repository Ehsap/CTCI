# Chapter VII - Technical Questions

# Example: Given an array of distinct integer values, count the number
# of pairs of integers that have difference k. For example, given the 
# array {1, 7, 5, 9, 2, 12, 3} and the difference k = 2, there are 
# four pairs with difference 2: (1, 3), (3, 5), (5, 7), (7, 9) .

def num_pairs(a, k):
    count = {}
    d = {} # {x: (x - k, x +k)}
    for x in a:
        d[x] = (x - k, x + k)
    
    for key, pair in d.iteritems():
        if pair[0] in d:
            if (pair[0], key) not in count: # Pair (1, 3) is the same as (3, 1), don't double count
                count[(key,pair[0])] = True
        elif pair[1] in d:
            if (pair[1], key) not in count:
                count[(key, pair[1])] = True
    
    return len(count)

# Example: Print all positive integer solutions to the equation a^3 + b^3 = c^2 + d^3 where
# a,b,c, and d are integers between 1 and 1000
# TODO:
import math
def solve_equation()
    n = 1000
    d = {} # {(c,d): []}
    for c in range(1,n):
        for d in range(1,n):
            result = int(math.pow(c, 3) + math.pow(d, 3))
            d[(c, d)] = result

# Example: Given a smaller string s and a bigger string b, design an algorithm to find all 
# permutations of the shorter string within the longer one. Print the location of each permutation.

# Example: Design an algorithm to print all permutations of a string. 
# For simplicity, assume all characters are unique.

# Example: Numbers are randomly generated and stored into an (expanding) array. 
# How would you keep track ofthe median?

