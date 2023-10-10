import unittest
import random
from typing import List

from quick_sort import quick_sort, quick_sort_1


class TestSort(unittest.TestCase):
    def test_quick_sort(self):
        a1 = self.new_nums()
        a2 = a1.copy()
        print(f"before sort: {a1}")
        a1 = quick_sort(a1)
        print(f"after quick_sort: {a1}")
        quick_sort_1(a2)
        print(f"after quick_sort_1: {a2}")
        self.assertEqual(a1, a2)

    def new_nums(self) -> List[int]:
        nums = []
        for _ in range(1024):
            nums.append(random.randint(-128, 127))
        return nums


if __name__ == "__main__":
    unittest.main()
