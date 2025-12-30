# Heap Practice Assignment (Python)

## Objective

Implement both min-heap and max-heap data structures from scratch using Python. Strengthen understanding of heap properties, tree representation, insertion/removal operations, and heap-based algorithms commonly asked in technical interviews.

---

## Part 1: Core Heap Implementation

### Task

Create two classes:

- `MinHeap`
- `MaxHeap`

Requirements:

1. Represent the heap internally using a Python list.
2. Implement the following methods:
   - `insert(value)`
   - `peek()` returns min or max without removal
   - `pop()` removes and returns min or max
   - `heapify_up(index)` helper
   - `heapify_down(index)` helper
   - `__len__` for convenience
3. Maintain heap property at all times.
4. Do **not** use `heapq`.

Deliverables:

- File: `heap.py`
- Include simple tests or assert checks demonstrating correctness.

---

## Part 2: Build Heap From Array

### Task

Implement a function:

build_heap(arr, heap_type='min'|'max')

Requirements:

1. Convert an unsorted list into a valid heap in **O(n)** time using bottom-up heapify.
2. Explain why this is O(n), not O(n log n).
3. Compare performance to inserting items one by one.

Deliverables:

- File: `build_heap.py` or integrated in `heap.py`
- Brief written explanation in the README.

---

## Part 3: Algorithms Using Your Heap

### A. K Smallest / K Largest Elements

Write:

k_smallest(nums, k)
k_largest(nums, k)

Variations:

- Implement using a min-heap.
- Implement using a max-heap.
- Note performance tradeoffs for small vs large K.

### B. Heap Sort

Use a **max-heap** to sort a list in ascending order.

Output example:
heap_sort([5,1,9,2]) -> [1,2,5,9]

### C. Running Median

Maintain a real-time running median stream.
add_num(x)
get_median()
