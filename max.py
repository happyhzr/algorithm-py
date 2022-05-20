from logging import exception
from typing import List


def max(a: List[int]) -> int:
    if a == []:
        raise Exception('list cant be empty list')
    return helper(a, 0, len(a)-1)


def helper(a: List[int], start: int, end: int) -> int:
    if start == end:
        return a[start]
    rest = helper(a, start+1, end)
    if a[start] > rest:
        return a[start]
    else:
        return rest


if __name__ == '__main__':
    print(max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(max([]))
