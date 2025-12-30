from heap import MinHeap, MaxHeap, Heap, build_heap

"""
Part A:

k_smallest(nums, k)
k_largest(nums, k)
"""


def k_smallest(nums, k):
    if k > len(nums):
        raise ValueError

    h = build_heap(nums, 'min')
    vals = [h.pop() for _ in range(k)]
    return vals


def k_largest(nums, k):
    if k > len(nums):
        raise ValueError

    h = build_heap(nums, 'max')
    vals = [h.pop() for _ in range(k)]
    return vals


"""
Part B:

Heap Sort
"""


def heap_sort(arr: list[int]) -> list[int]:
    # given an arr of ints, return sorted array
    # count up, e.g. [1, 1, 3, 4]
    # 1. re-order arr to be a max_heap
    for i in range(len(arr)//2 - 1, -1, -1):
        heapify_down(arr, i, len(arr))
    # 2. swap root with last element, decrease size by one, heapify new root
    # 3. repeat #2 until size is 1, and whole array is sorted
    size = len(arr)
    while size > 1:
        arr[0], arr[size-1] = arr[size-1], arr[0]
        size -= 1
        heapify_down(arr, 0, size)
    return arr


def heapify_down(arr, index, size):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < size and arr[left] > arr[largest]:
        largest = left
    if right < size and arr[right] > arr[largest]:
        largest = right

    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        heapify_down(arr, largest, size)


"""
Part C:

Running Median
add_num(x)
get_median()
"""


class Median:
    def __init__(self, nums):
        self.max_heap = MaxHeap()  # lower half
        self.min_heap = MinHeap()  # upper half

        for n in nums:
            self.add_num(n)

    def add_num(self, num):
        # keep the lower half of all numbers in the max heap, and the upper
        # half of all numbers in the min heap
        if not self.max_heap or num <= self.max_heap.peek():
            self.max_heap.insert(num)
        else:
            self.min_heap.insert(num)

        if len(self.min_heap) - len(self.max_heap) > 1:
            val = self.min_heap.pop()
            self.max_heap.insert(val)
        if len(self.max_heap) - len(self.min_heap) > 1:
            val = self.max_heap.pop()
            self.min_heap.insert(val)

    def get_median(self):
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap.peek()
        elif len(self.max_heap) > len(self.min_heap):
            return self.max_heap.peek()
        else:
            return (self.max_heap.peek() + self.min_heap.peek()) / 2
