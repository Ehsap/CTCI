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

# 10.3 Search in Rotated Array: Given a sorted array of n 
# integers that has been rotated an uknown number of times,
# write code to find an element in the array. You may
# assume that the array was originally sorted in increasing order.

def search_rotated_array(A, k):
    # Empty Array
    if len(A) == 0:
        return -1
    # Array of Length 1
    if len(A) == 1:
        if A[0] == k:
            return 0

    # Find how many times the array has been shifted by
    shifts = 0
    for i in range(len(A) - 1):
        if A[i + 1] < A[i]:
            shifts = i
            break
    # Binary search through the array using the shifts
    low = 0
    mid = (len(A)//2)
    high = len(A) - 1

    while low < high:
        mid = (low + high) // 2
        if k < A[(mid + shifts) % len(A)]:
            high = mid 
        elif k > A[(mid + shifts) % len(A)]:
            low = mid + 1
        else:
            return (mid + shifts) % len(A)
    return -1

# 10.4 Sorted Search, No Size
class Listy:
    def __init__(self):
        self.arr = []

    def set_list(self, A):
        self.arr = A
    
    def elementAt(self, i):
        try:
            return self.arr[i]
        except IndexError:
            return -1
    
    def search(self, x):
        i = 1
        while self.elementAt(i) != -1 and self.elementAt(i) < x:
            i *= 2
        return self.binarySearch(x, 0, i)
    
    def binarySearch(self, x, low, high):
        mid = 0 
        while low <= high:
            mid = (low + high) // 2
            middle = self.elementAt(mid)
            if x == middle:
                return mid
            elif x > middle:
                low = mid + 1
            else:
                high = mid - 1
        return -1

# 10.5 Sparse Search
# Given a sorted array of strings that is interspersed with
# empty strings, write a method to find the location
# of a given string.
def sparse_search(A, value):
    if len(A) == 0:
        return -1
    elif len(A) == 1:
        if A[0] == value:
            return 0
        else:
            return -1 
    else:
        return sparse_search_aux(A, value, 0, len(A)-1)

def sparse_search_aux(A, value, low, high):
    if (low > high):
        return - 1
    mid = (low + high) // 2
    
    if A[mid] == "":
        left = mid-1
        right = mid+1
        while True:
            if left < low and right > high:
                return -1
            elif right <= high and A[right] != "":
                mid = right
                break
            elif left >= low and A[left] != "":
                mid = left
                break
            right += 1
            left -= 1

    if A[mid] == value:
        return mid
    elif A[mid] < value:
        return sparse_search_aux(A, value, mid+1, high)
    else:
        return sparse_search_aux(A, value, low, mid-1)

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
    
    def test_search_rotated_array(self):
        A = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
        self.assertEquals(search_rotated_array(A, 5), 8)
        self.assertEquals(search_rotated_array(A, 21), -1)

    def test_sorted_search_no_size(self):
        l = Listy()
        l.set_list([2,4,5,9,10,22,33,29])
        self.assertEqual(l.search(10), 4)
        self.assertEqual(l.search(29), -1)
    
    def test_sparse_search(self):
        self.assertEqual(sparse_search(["at", "", "", "ball", "", "", "car"], "at"), 0)
    
if __name__ == '__main__':
    unittest.main()