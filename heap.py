"""
This module contains the Heap superclass, and both the MinHeap and MaxHeap
subclasses
"""


class Heap:
    """
    The super class for both MinHeap and MaxHeap
    """

    def __init__(self):
        self.values = []

    def __len__(self):
        return len(self.values)

    def peek(self):
        """
        Return the top value of the heap without effecting the heap.
        """
        return self.values[0]

    def pop(self):
        """
        Remove and return the top value of the heap.
        """
        if len(self.values) == 0:
            raise IndexError("pop from empty heap")

        val = self.peek()

        self.values[0] = self.values[-1]
        self.values.pop()
        self.heapify_down(0)

        return val

    def delete(self):
        """
        delete the top value of the heap without returning anything
        """
        self.pop()

    def insert(self, value):
        """
        Insert the given value into the heap maintaining proper heap ordering.

        :param value: the value to be inserted into the heap
        """
        self.values.append(value)
        self.heapify_up(len(self) - 1)

    def heapify_up(self, index):
        """
        Bubble-up/sift-up the value at the given index until all heap properties
        are satisfied.

        :param index: the index of the value to move
        """
        raise NotImplementedError("heapify_up must be implemented by subclass")

    def heapify_down(self, index):
        """
        Bubble-down/sift-down the value at the given index until all heap
        properties are satisfied.

        :param index: the index of the value to move
        """
        raise NotImplementedError(
            "heapify_down must be implemented by subclass")


class MinHeap(Heap):
    """
    An implementation for a MinHeap
        - a complete binary tree (all level filled, except bottom)
        - value of root must be the SMALLEST among all its descendants and the
          same is true for all left and right subtrees
    """

    def heapify_up(self, index):
        """
        Compare the new element with its parent. If the parent is greater than 
        the new element, swap them.
        Repeat step 2 until the parent is smaller than or equal to the new 
        element, or until the new element reaches the root of the tree.
        """
        parent_index = (index - 1) // 2
        if index > 0 and self.values[parent_index] > self.values[index]:
            self.values[parent_index], self.values[index] = self.values[index], self.values[parent_index]
            self.heapify_up(parent_index)

    def heapify_down(self, index):
        """
        Repeatedly compare index value with its children.
        Swap it with the smaller child (min-heap) or larger child (max-heap).
        Continue until it is in the correct position.
        """
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self) and self.values[left] < self.values[smallest]:
            smallest = left
        if right < len(self) and self.values[right] < self.values[smallest]:
            smallest = right

        if smallest != index:
            self.values[index], self.values[smallest] = self.values[smallest], self.values[index]
            self.heapify_down(smallest)


class MaxHeap(Heap):
    """
    An implementation for a MaxHeap
        - a complete binary tree (all level filled, except bottom)
        - value of root must be the LARGEST among all its descendants and the
          same is true for all left and right subtrees
    """

    def heapify_up(self, index):
        """
        Compare the new element with its parent. If the parent is less than 
        the new element, swap them.
        Repeat step 2 until the parent is greater than or equal to the new 
        element, or until the new element reaches the root of the tree.
        """
        parent_index = (index - 1) // 2
        if index > 0 and self.values[parent_index] < self.values[index]:
            self.values[index], self.values[parent_index] = self.values[parent_index], self.values[index]
            self.heapify_up(parent_index)

    def heapify_down(self, index):
        """
        Repeatedly compare index value with its children.
        Swap it with the smaller child (min-heap) or larger child (max-heap).
        Continue until it is in the correct position.
        """
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self) and self.values[left] > self.values[largest]:
            largest = left
        if right < len(self) and self.values[right] > self.values[largest]:
            largest = right

        if largest != index:
            self.values[index], self.values[largest] = self.values[largest], self.values[index]
            self.heapify_down(largest)


def build_heap(arr, heap_type=str):
    """
    Given an array and a heap_type, construct and return a heap of the 
    given type with the given values in correct heap ordering.

    :param arr: a list of values
    :param heap_type: the type of heap, either min or max
    """
    match heap_type:
        case 'min':
            h = MinHeap()
        case 'max':
            h = MaxHeap()
        case _:
            raise ValueError("Invalid Heap Type")

    # place all values from arr into the heap
    h.values = arr
    # use heapify_down to ensure proper ordering of all values
    for index in range(len(h)//2 - 1, -1, -1):
        h.heapify_down(index)

    return h
