from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums1:
            nums1 = nums2
            return nums1

        if not nums2:
            return nums1

        if nums1[0] > nums2[0]:
            nums1.insert(0, nums2[0])
            nums1.pop()
            nums2.pop(0)

        for i in range(m+n):
            if not nums2:
                break
            if nums1[i] == 0 and m == 0:
                nums1[i] = nums2.pop(0)
            if nums1[i] == 0 and i >= m and m > n:
                nums1[i] = nums2.pop(0)
            if nums1[i] == 0 and i >= n and m < n:
                nums1[i] = nums2.pop(0)
            if i < m+n-1:
                if nums1[i] <= nums2[0] <= nums1[i+1]:
                    nums1.insert(i+1, nums2[0])
                    nums1.pop()
                    nums2.pop(0)

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
