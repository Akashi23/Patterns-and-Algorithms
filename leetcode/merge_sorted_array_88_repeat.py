from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Initialize nums1's index
        i = m - 1
        # Initialize nums2's index
        j = n - 1
        # Initialize a variable k to store the last index of the 1st array...
        k = m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1

        return nums1


solution = Solution()
answer = solution.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
print(answer)
assert answer == [1, 2, 2, 3, 5, 6]

answer = solution.merge([1], 1, [], 0)
print(answer)
assert answer == [1]

answer = solution.merge([2, 0], 1, [1], 1)
print(answer)
assert answer == [1, 2]

answer = solution.merge([-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 2], 3)
print(answer)
assert answer == [-1, 0, 0, 1, 2, 2, 3, 3, 3]

answer = solution.merge([0], 0, [1], 1)
print(answer)
assert answer == [1]

answer = solution.merge([1, 0], 1, [2], 1)
print(answer)
assert answer == [1, 2]

answer = solution.merge([4, 0, 0, 0, 0, 0], 1, [1, 2, 3, 5, 6], 5)
print(answer)
assert answer == [1, 2, 3, 4, 5, 6]

answer = solution.merge([-1, 3, 0, 0, 0, 0, 0], 2, [0, 0, 1, 2, 3], 5)
print(answer)
assert answer == [-1, 0, 0, 1, 2, 3, 3]
