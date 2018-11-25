# Chapter 2 - Linked Lists

# Singly Linked List
class MyLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    
    def __init__(self):
        self.head = None
    
    def appendLast(data):
        n = Node(data)
        if self.isEmpty()
            self.head = n
            return self.head
        
        pointer = self.head
        # Go all the way to the end of the list
        while (pointer.next != None):
            pointer = pointer.next
        pointer.next = n 
        return self.head

    def isEmpty(self):
        return self.head == None  

# 2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list
# Follow up: How would you solve this problem if a temporary bufer isn't allowed?
    def remove_dups(self):
        # Dictionary that stores used values 
        used = {}

        # Go through linked list and add data to the used dictionary
        n = self.head 
        while n != None:
            if n.data not in used:
                used[n.data] = True
            else:
                # Check if last node
                if n.next = None
                    n = None 
                else:
                # Remove this node in the middle of the list
                n.next = n.next.next
            n = n.next 
        return self.head 

# 2.2 Return Kth to Last: Implement an algorithm to find the kth to last
# element of a singly linked list
    def k_to_last(self,k):
        if self.isEmpty():
            raise('EmptyLinkedListException')
        # Go to the end of the list

        # Go back k nodes and return it


