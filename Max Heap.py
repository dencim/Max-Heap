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
        self.build_max_heap() #Auto builds max heap from input array
        
    #Builds max heap from any array
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
    #Returns max item in heap
    def heap_max(self):
        return self.heap[0]

    #Returns, removes, and fixes back into valid heap
    def extract_max(self):
        extracted = self.heap_max()
        
        #Fix heap if there is elements to fix
        if len(self.heap) > 1:
            self.heap[0] = self.heap.pop(-1)
            self.max_heapify(0)
        
        return extracted
    
    #Inserts item into heap
    def insert(self, x):
        self.heap.append(x)
        i = len(self.heap)
        while( self.heap[i-1] > self.heap[self.parent(i)-1]):
            #swap
            temp = self.heap[self.parent(i)-1]
            self.heap[self.parent(i)-1] = self.heap[i-1]
            self.heap[i-1] = temp
            i = self.parent(i-1)
            
    def heap_sort(self):
        sorted = []
        
        for i in range(0, len(self.heap)):
            sorted.insert(0,self.extract_max())
        
        
        return sorted
    
    #Prints heap as an array
    def print_as_array(self):
        print(self.heap)
    
    #Prints heap as tree
    def print_as_tree(self):
         self.printing(1, 0)
         
    #Helper functions
    def left_child(self, i):
        return 2*i
    def right_child(self, i):
        return 2 * i + 1
    def parent(self, i):
        return int(( i  / 2 ))
    
    #Helper funtion for printing
    def printing(self, i, debth) :
        
        if len(self.heap) < i:
            return
        
        right = self.right_child(i)  
        left = self.left_child(i)
        
        
        debth += 1
        self.printing(right, debth)
        
        
        print("   " * debth, end =" ")
        print(self.heap[i-1])
        
        self.printing(left, debth)
            
        
#Test code
h = MaxHeap([4,1,3,2,16,9,10,14,8,7])
print("Tree: ")
h.print_as_tree()
print("Array: ")
h.print_as_array()
print("Sorted : ", h.heap_sort())

