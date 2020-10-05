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
        self.build_max_heap()
        
    def build_max_heap(self):
        for i in range(int(len(self.heap)/2) -1, -1, -1):
            #print("maxing at ", i)
            self.max_heapify(i)
        
    #Takes index at where to max heapify - input i is indexed from 0
    def max_heapify(self, i):
        #print(self.heap)
        
        i = i+1 #bc indexing from 1
        
        left = self.left_child(i)
        #print("Left ", left)
        right = self.right_child(i)
        #print("right ", right)
        
        #if left child exists and value at child is greater then parent
        if left <= len(self.heap) and self.heap[left-1] > self.heap[i-1]:
            largest = left
            #print("largest left ", largest)
        else:
            largest = i
        
        #if right child exists and value at child is greater then max( parent and left child)
        if right <= len(self.heap) and self.heap[right-1] > self.heap[largest-1]:
            largest = right
            #print("largest right ", largest)
        if largest != i:
            #print("largest:", largest)
            #Exchange A[i] with A[largest]
            temp = self.heap[largest-1]
            self.heap[largest-1] = self.heap[i-1]
            self.heap[i-1] = temp
            
            
            self.max_heapify(largest-1)
    
    def heap_max(self):
        return self.heap[0]

    def extract_max(self):
        extracted = self.heap_max()
        
        #Fix heap
        self.heap[0] = self.heap.pop(-1)
        self.max_heapify(0)
        
        return extracted
    
    def insert(self, x):
        self.heap.append(x)
        i = len(self.heap)
        while( self.heap[i-1] > self.heap[self.parent(i)-1]):
            #swap
            temp = self.heap[self.parent(i)-1]
            self.heap[self.parent(i)-1] = self.heap[i-1]
            self.heap[i-1] = temp
            i = self.parent(i-1)
    
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
            
#h = MaxHeap([16,4,10,14,7,9,3,2,8,1])
h2 = MaxHeap([4,1,3,2,16,9,10,14,8,7])
h3 = MaxHeap([16,14,10,8,7,9,3,2,4,1])
#h.print_as_tree()
#h.max_heapify(1)
#h.print_as_array()
#h2.print_as_array()
#print(h2.extract_max())
h2.print_as_array()
h3.insert(15)
h3.print_as_array()