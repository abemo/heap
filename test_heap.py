# test_heap.py
# Run using: pytest test_heap.py
import pytest
from heap import MinHeap, MaxHeap, Heap, build_heap


def test_len_empty_heap():
    h = MinHeap()
    assert len(h) == 0

    h = MaxHeap()
    assert len(h) == 0


def test_peek_single_element():
    h = MinHeap()
    h.insert(10)
    assert h.peek() == 10

    h = MaxHeap()
    h.insert(20)
    assert h.peek() == 20


def test_insert_minheap_ordering():
    h = MinHeap()
    for v in [5, 3, 8, 1, 6]:
        h.insert(v)

    assert h.peek() == 1         # smallest should be root
    assert sorted(h.values) == sorted([5, 3, 8, 1, 6])  # same elements present


def test_insert_maxheap_ordering():
    h = MaxHeap()
    for v in [5, 3, 8, 1, 6]:
        h.insert(v)

    assert h.peek() == 8         # largest should be root
    assert sorted(h.values) == sorted([5, 3, 8, 1, 6])  # same elements present


def test_pop_minheap():
    h = MinHeap()
    for v in [5, 3, 8, 1, 6]:
        h.insert(v)

    popped = h.pop()
    assert popped == 1           # smallest removed
    assert len(h) == 4


def test_pop_maxheap():
    h = MaxHeap()
    for v in [5, 3, 8, 1, 6]:
        h.insert(v)

    popped = h.pop()
    assert popped == 8           # largest removed
    assert len(h) == 4


def test_multiple_pop_minheap():
    h = MinHeap()
    values = [9, 4, 7, 1, 3]
    for v in values:
        h.insert(v)

    results = [h.pop(), h.pop(), h.pop(), h.pop(), h.pop()]
    assert results == sorted(values)


def test_multiple_pop_maxheap():
    h = MaxHeap()
    values = [9, 4, 7, 1, 3]
    for v in values:
        h.insert(v)

    results = [h.pop(), h.pop(), h.pop(), h.pop(), h.pop()]
    assert results == sorted(values, reverse=True)


def test_peek_does_not_modify_heap():
    h = MinHeap()
    for v in [4, 2, 5]:
        h.insert(v)

    top = h.peek()
    assert top == 2
    assert len(h) == 3           # no removal


def test_heap_pop_until_empty_minheap():
    h = MinHeap()
    for v in [10, 2, 14]:
        h.insert(v)

    assert h.pop() == 2
    assert h.pop() == 10
    assert h.pop() == 14
    assert len(h) == 0


def test_heap_pop_until_empty_maxheap():
    h = MaxHeap()
    for v in [10, 2, 14]:
        h.insert(v)

    assert h.pop() == 14
    assert h.pop() == 10
    assert h.pop() == 2
    assert len(h) == 0


def test_peek_raises_on_empty_heap():
    h = MinHeap()
    with pytest.raises(IndexError):
        h.peek()

    h = MaxHeap()
    with pytest.raises(IndexError):
        h.peek()


def test_pop_raises_on_empty_heap():
    h = MinHeap()
    with pytest.raises(IndexError):
        h.pop()

    h = MaxHeap()
    with pytest.raises(IndexError):
        h.pop()


def is_min_heap(values):
    """Utility: verify min-heap property."""
    n = len(values)
    for i in range(n):
        left, right = 2*i + 1, 2*i + 2
        if left < n and values[i] > values[left]:
            return False
        if right < n and values[i] > values[right]:
            return False
    return True


def is_max_heap(values):
    """Utility: verify max-heap property."""
    n = len(values)
    for i in range(n):
        left, right = 2*i + 1, 2*i + 2
        if left < n and values[i] < values[left]:
            return False
        if right < n and values[i] < values[right]:
            return False
    return True


# ------------------ TESTS ------------------ #

def test_build_min_heap_basic():
    arr = [5, 3, 8, 1, 4]
    h = build_heap(arr, heap_type='min')
    assert isinstance(h, MinHeap)
    assert is_min_heap(h.values)


def test_build_max_heap_basic():
    arr = [5, 3, 8, 1, 4]
    h = build_heap(arr, heap_type='max')
    assert isinstance(h, MaxHeap)
    assert is_max_heap(h.values)


def test_min_heap_order_after_pops():
    arr = [9, 4, 7, 1, 3, 6]
    h = build_heap(arr, heap_type='min')
    assert is_min_heap(h.values)
    popped = [h.pop(), h.pop(), h.pop()]
    assert is_min_heap(h.values)
    assert popped == [1, 3, 4]


def test_max_heap_order_after_pops():
    arr = [9, 4, 7, 1, 3, 6]
    h = build_heap(arr, heap_type='max')
    assert (is_max_heap(h.values))
    popped = [h.pop(), h.pop(), h.pop()]
    assert popped == [9, 7, 6]


def test_build_heap_empty():
    h = build_heap([], heap_type='min')
    assert len(h.values) == 0


def test_build_heap_single_element():
    h = build_heap([10], heap_type='max')
    assert h.values == [10]


def test_build_heap_duplicates():
    arr = [5, 5, 5, 5]
    h = build_heap(arr, heap_type='min')
    assert is_min_heap(h.values)
    assert len(h.values) == 4


def test_invalid_heap_type():
    with pytest.raises(Exception):
        build_heap([1, 2, 3], heap_type='banana')
