"""
Python program for Bitonic Sort.
Note that this program works only when size of input is a power of 2.
"""

from __future__ import annotations

# web solution

#License:  https://bit.ly/2InTS3W 
# Python program for Bitonic Sort. Note that this program 
# works only when size of input is a power of 2. 
# The parameter dir indicates the sorting direction, ASCENDING 
# or DESCENDING; if (a[i] > a[j]) agrees with the direction, 
# then a[i] and a[j] are interchanged.
def compAndSwap(a, i, j, dire):
    if (dire == 1 and a[i] > a[j]) or (dire == 0 and a[i] < a[j]):
        a[i], a[j] = a[j], a[i]
        # It recursively sorts a bitonic sequence in ascending order,
# if dir = 1, and in descending order otherwise (means dir=0).
# The sequence to be sorted starts at index position low, 
# the parameter cnt is the number of elements to be sorted. 
def bitonicMerge(a, low, cnt, dire):
    if cnt > 1:
        k = int(cnt / 2)
        for i in range(low, low + k):
            compAndSwap(a, i, i + k, dire)
        bitonicMerge(a, low, k, dire)
        bitonicMerge(a, low + k, k, dire)

        # This funcion first produces a bitonic sequence by recursively


# sorting its two halves in opposite sorting orders, and then
# calls bitonicMerge to make them in the same order 
def bitonicSort(a, low, cnt, dire):
    if cnt > 1:
        k = int(cnt / 2)
        bitonicSort(a, low, k, 1)
        bitonicSort(a, low + k, k, 0)
        bitonicMerge(a, low, cnt, dire)

        # Caller of bitonicSort for sorting the entire array of length N


# in ASCENDING order
def sort(a, N, up):
    bitonicSort(a, 0, N, up)


# https://github.com/TheAlgorithms/Python/blob/master/sorts/bitonic_sort.py

def comp_and_swap(array: list[int], index1: int, index2: int, direction: int) -> None:
    """Compare the value at given index1 and index2 of the array and swap them as per
    the given direction.
    The parameter direction indicates the sorting direction, ASCENDING(1) or
    DESCENDING(0); if (a[i] > a[j]) agrees with the direction, then a[i] and a[j] are
    interchanged.
    >>> arr = [12, 42, -21, 1]
    >>> comp_and_swap(arr, 1, 2, 1)
    >>> print(arr)
    [12, -21, 42, 1]
    >>> comp_and_swap(arr, 1, 2, 0)
    >>> print(arr)
    [12, 42, -21, 1]
    >>> comp_and_swap(arr, 0, 3, 1)
    >>> print(arr)
    [1, 42, -21, 12]
    >>> comp_and_swap(arr, 0, 3, 0)
    >>> print(arr)
    [12, 42, -21, 1]
    """
    if (direction == 1 and array[index1] > array[index2]) or (
        direction == 0 and array[index1] < array[index2]
    ):
        array[index1], array[index2] = array[index2], array[index1]

def bitonic_merge(array: list[int], low: int, length: int, direction: int) -> None:
    """
    It recursively sorts a bitonic sequence in ascending order, if direction = 1, and in
    descending if direction = 0.
    The sequence to be sorted starts at index position low, the parameter length is the
    number of elements to be sorted.
    >>> arr = [12, 42, -21, 1]
    >>> bitonic_merge(arr, 0, 4, 1)
    >>> print(arr)
    [-21, 1, 12, 42]
    >>> bitonic_merge(arr, 0, 4, 0)
    >>> print(arr)
    [42, 12, 1, -21]
    """
    if length > 1:
        middle = int(length / 2)
        for i in range(low, low + middle):
            comp_and_swap(array, i, i + middle, direction)
        bitonic_merge(array, low, middle, direction)
        bitonic_merge(array, low + middle, middle, direction)


def bitonic_sort(array: list[int], low: int, length: int, direction: int) -> None:
    """
    This function first produces a bitonic sequence by recursively sorting its two
    halves in opposite sorting orders, and then calls bitonic_merge to make them in the
    same order.
    >>> arr = [12, 34, 92, -23, 0, -121, -167, 145]
    >>> bitonic_sort(arr, 0, 8, 1)
    >>> arr
    [-167, -121, -23, 0, 12, 34, 92, 145]
    >>> bitonic_sort(arr, 0, 8, 0)
    >>> arr
    [145, 92, 34, 12, 0, -23, -121, -167]
    """
    if length > 1:
        middle = int(length / 2)
        bitonic_sort(array, low, middle, 1)
        bitonic_sort(array, low + middle, middle, 0)
        bitonic_merge(array, low, length, direction)

# tests
if __name__ == "__main__":

    _test = 'web2'
    if _test == 'web1' :
        # Driver code to test above
        a = []
        print("How many numbers u want to enter?");
        n = int(input())
        print("Input the numbers:");
        for i in range(n):
            a.append(int(input()))
        up = 1

        sort(a, n, up)
        print("\n\nSorted array is:")
        for i in range(n):
            print("%d" % a[i])

    if _test == 'web2' :
        user_input = input("Enter numbers separated by a comma:\n").strip()
        unsorted = [int(item.strip()) for item in user_input.split(",")]

        bitonic_sort(unsorted, 0, len(unsorted), 1)
        print("\nSorted array in ascending order is: ", end="")
        print(*unsorted, sep=", ")

        bitonic_merge(unsorted, 0, len(unsorted), 0)
        print("Sorted array in descending order is: ", end="")
        print(*unsorted, sep=", ")
