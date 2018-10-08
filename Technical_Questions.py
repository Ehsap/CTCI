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
