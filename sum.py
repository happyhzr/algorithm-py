from typing import List


def sum(a: List[int]) -> int:
    return helper(a, 0, len(a)-1)


def helper(a: List[int], start: int, end: int) -> int:
    if start > end:
        return 0
    return a[start]+helper(a, start+1, end)


if __name__ == '__main__':
    print(sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(sum([]))
