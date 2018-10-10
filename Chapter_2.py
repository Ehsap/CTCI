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
        if self.head = None:
            self.head = n
            return self.head
        
        pointer = self.head
        # Go all the way to the end of the list
        while (pointer.next != None):
            pointer = pointer.next
        pointer.next = n 
        return self.head 
            

# 2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list
# Follow up: How would you solve this problem if a temporary bufer isn't allowed?

