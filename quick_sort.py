from typing import List


def quick_sort(a: List[int]) -> None:
    if a == []:
        return a
    pivot = a[0]
    less = [i for i in a[1:] if i <= pivot]
    greater = [i for i in a[1:] if i > pivot]
    return quick_sort(less)+[pivot]+quick_sort(greater)


def quick_sort_1(a: List[int]) -> None:
    qsort(a, 0, len(a)-1)


def qsort(a: List[int], start: int, end: int):
    if start >= end:
        return
    pivot_new_i = partition(a, start, end, start)
    qsort(a, start, pivot_new_i-1)
    qsort(a, pivot_new_i+1, end)


def partition(a: List[int], start: int, end: int, pivot_i: int) -> int:
    pivot_v = a[pivot_i]
    a[pivot_i], a[end] = a[end], a[pivot_i]
    store_i = start
    for i in range(start, end):
        if a[i] < pivot_v:
            a[i], a[store_i] = a[store_i], a[i]
            store_i += 1
    a[store_i], a[end] = a[end], a[store_i]
    return store_i
