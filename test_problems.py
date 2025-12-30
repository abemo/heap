# test_problems.py
# Run using: pytest test_problems.py

import pytest
from heap_problems import k_smallest, k_largest, heap_sort, Median

# ------------------- k_smallest ------------------- #


def test_k_smallest_basic():
    nums = [5, 1, 3, 6, 4, 2]
    assert k_smallest(nums, 3) == [1, 2, 3]


def test_k_smallest_all_elements():
    nums = [5, 1, 3]
    assert k_smallest(nums, 3) == [1, 3, 5]


def test_k_smallest_empty_array():
    nums = []
    assert k_smallest(nums, 0) == []


def test_k_smallest_k_zero():
    nums = [5, 1, 3]
    assert k_smallest(nums, 0) == []


def test_k_smallest_with_duplicates():
    nums = [4, 2, 4, 1, 3, 2]
    assert k_smallest(nums, 4) == [1, 2, 2, 3]


def test_k_smallest_negative_numbers():
    nums = [-5, -1, -3, 0, 2]
    assert k_smallest(nums, 3) == [-5, -3, -1]

# ------------------- k_largest ------------------- #


def test_k_largest_basic():
    nums = [5, 1, 3, 6, 4, 2]
    assert k_largest(nums, 3) == [6, 5, 4]


def test_k_largest_all_elements():
    nums = [5, 1, 3]
    assert k_largest(nums, 3) == [5, 3, 1]


def test_k_largest_empty_array():
    nums = []
    assert k_largest(nums, 0) == []


def test_k_largest_k_zero():
    nums = [5, 1, 3]
    assert k_largest(nums, 0) == []


def test_k_largest_with_duplicates():
    nums = [4, 2, 4, 1, 3, 2]
    assert k_largest(nums, 4) == [4, 4, 3, 2]


def test_k_largest_negative_numbers():
    nums = [-5, -1, -3, 0, 2]
    assert k_largest(nums, 3) == [2, 0, -1]

# ------------------- edge cases ------------------- #


def test_k_larger_than_length_smallest():
    nums = [3, 1, 2]
    with pytest.raises(ValueError):
        k_smallest(nums, 5)


def test_k_larger_than_length_largest():
    nums = [3, 1, 2]
    with pytest.raises(ValueError):
        k_largest(nums, 5)


# ------------------- heap sort tests ------------------- #

# ------------------- Basic tests ------------------- #

def test_heap_sort_basic():
    arr = [5, 3, 8, 1, 4, 2]
    assert heap_sort(arr) == sorted(arr)


def test_heap_sort_single_element():
    arr = [42]
    assert heap_sort(arr) == [42]


def test_heap_sort_empty():
    arr = []
    assert heap_sort(arr) == []


def test_heap_sort_duplicates():
    arr = [4, 2, 4, 1, 3, 2]
    assert heap_sort(arr) == sorted(arr)


def test_heap_sort_negative_numbers():
    arr = [-5, -1, -3, 0, 2]
    assert heap_sort(arr) == sorted(arr)

# ------------------- Edge cases ------------------- #


def test_heap_sort_already_sorted():
    arr = [1, 2, 3, 4, 5]
    assert heap_sort(arr) == [1, 2, 3, 4, 5]


def test_heap_sort_reverse_sorted():
    arr = [5, 4, 3, 2, 1]
    assert heap_sort(arr) == [1, 2, 3, 4, 5]


def test_heap_sort_large_random():
    import random
    arr = random.sample(range(1000), 100)  # 100 unique random numbers
    assert heap_sort(arr) == sorted(arr)


# ------------------- Running Median tests ------------------- #

# ------------------- Basic tests ------------------- #

def test_median_initial_list_odd():
    nums = [1, 3, 2]
    m = Median(nums)
    assert m.get_median() == 2  # median of [1,2,3] is 2


def test_median_initial_list_even():
    nums = [1, 2, 3, 4]
    m = Median(nums)
    # median of [1,2,3,4] is (2+3)/2
    assert m.get_median() == 2.5

# ------------------- Incremental addition ------------------- #


def test_median_add_numbers():
    m = Median([])
    m.add_num(1)
    assert m.get_median() == 1
    m.add_num(2)
    assert m.get_median() == 1.5
    m.add_num(3)
    assert m.get_median() == 2
    m.add_num(4)
    assert m.get_median() == 2.5
    m.add_num(5)
    assert m.get_median() == 3


def test_median_with_duplicates():
    m = Median([2, 2, 2])
    assert m.get_median() == 2
    m.add_num(2)
    assert m.get_median() == 2
    m.add_num(3)
    assert m.get_median() == 2


def test_median_with_negatives():
    m = Median([-3, -1, -2])
    assert m.get_median() == -2
    m.add_num(-4)
    assert m.get_median() == -2.5
    m.add_num(0)
    assert m.get_median() == -2

# ------------------- Single element ------------------- #


def test_median_single_element():
    m = Median([42])
    assert m.get_median() == 42
    m.add_num(10)
    assert m.get_median() == 26  # (42+10)/2

# ------------------- Random order stream ------------------- #


def test_median_random_stream():
    stream = [5, 15, 1, 3]
    m = Median([])
    medians = []
    for n in stream:
        m.add_num(n)
        medians.append(m.get_median())
    assert medians == [5, 10, 5, 4]  # incremental medians
