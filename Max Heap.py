# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 23:24:15 2020

@author: denis
Part 4
"""

class MaxHeap:
    
    heap = []
    
    def __init__(self, heap=[]):
        #do code for build-max heap here
        self.heap = heap
        
    #Takes index at where to max heapify
    def max_heapify(self, i):
        print(self.heap)
        
        i = i+1 #bc indexing from 1
        
        left = self.left_child(i)
        print("Left ", left)
        right = self.right_child(i)
        print("right ", right)
        
        #if left child exists and value at child is greater then parent
        if left <= len(self.heap) and self.heap[left-1] > self.heap[i-1]:
            largest = left
            print("largest left ", largest)
        else:
            largest = i
        
        #if right child exists and value at child is greater then max( parent and left child)
        if right <= len(self.heap) and self.heap[right-1] > self.heap[largest-1]:
            largest = right
            print("largest right ", largest)
        if largest != i:
            print("largest:", largest)
            #Exchange A[i] with A[largest]
            temp = self.heap[largest-1]
            self.heap[largest-1] = self.heap[i-1]
            self.heap[i-1] = temp
            
            
            self.max_heapify(largest-1)
    
    def heap_max(self):
        return self.heap[0]

    def extract_max(self):
        extracted = self.heap_max()
        #Fix heap here
        return extracted
    
    def insert(self):
        pass
    
    def print_as_array(self):
        print(self.heap)
    
    def print_as_tree(self):
        #change to work
        for i in self.heap:
            print(i)    
    #Helper functions
    def left_child(self, i):
        return 2*i
    def right_child(self, i):
        return 2 * i + 1
    def parent(self, i):
        return int(( i  / 2 ))
            
h = MaxHeap([16,4,10,14,7,9,3,2,8,1])
#h.print_as_array()
#h.print_as_tree()
h.max_heapify(1)
h.print_as_array()