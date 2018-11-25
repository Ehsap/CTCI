import unittest
# Chapter 10 - Sorting and Searching 

# 10. 1 Sorted Merge
# You are given two sorted arrays, A and B, where A has
# a large enough buffer at the end to hold B. Write a 
# method to merge B into A in sorted order

def sorted_merge(A, B):
    
    num_elems_A = 0
    i = 0
    # Find number of elements in A
    while A[i] is not None:
        num_elems_A += 1
        i += 1

    # Shift all elements of A to the buffer space
    for i in range(0, num_elems_A):
        A[i + len(B)] = A[i]
        A[i] = 0

    # Merge A and B
    i = len(B) # Iterate through A array
    j = 0 # Iterate through B array
    k = 0 # Position to merge elems
    
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            A[k] = A[i]
            i += 1
            k += 1
        else:
            A[k] = B[j]
            j += 1
            k += 1
    
    # Fill remaining numbers from A or B
    while i < len(A):
        A[k] = A[i]
        i += 1
        k += 1
    while j < len(B):
        A[k] = B[j]
        j += 1
        k += 1
    return A

# 10.2 Group Anagrams: Write a method to sort an 
# array of strings so that all the anagrams are next
# to each other
def group_anagrams(strings):
    anagrams = []
    anagram_indices = {} # "ate": [1,2,3]
    # Sort every string and place into dictionary
    for i in range(len(strings)):
        sorted_word = ''.join(sorted(strings[i]))
        if sorted_word not in anagram_indices:
            anagram_indices[sorted_word] = [i]
        else:
            anagram_indices[sorted_word].append(i)
    
    # Build the anagram groupings
    for indices in anagram_indices.values():
        anagram_group = []
        for index in indices:
            anagram_group.append(strings[index])
        anagrams.append(anagram_group)
    return anagrams



class Tests(unittest.TestCase):

    def test_sorted_merge(self):
        A = [5, 6, 7, None, None, None]
        B = [1, 2, 3]
        self.assertEquals(sorted_merge(A,B), [1,2,3,5,6,7]) 
        A = [1, None, None, None]
        B = [2, 5, 8]
        self.assertEquals(sorted_merge(A, B), [1,2,5,8])
        A = [1, None]
        B = [2]
        self.assertEquals(sorted_merge(A,B), [1,2])
    
if __name__ == '__main__':
    unittest.main()