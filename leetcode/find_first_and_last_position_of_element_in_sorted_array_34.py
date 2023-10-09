from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        targetIndex = self.binary_search(nums, target)

        if targetIndex is None:
            return [-1, -1]

        rightPos = targetIndex + 1
        leftPos = targetIndex - 1

        if rightPos >= len(nums):
            rightPos = len(nums) - 1

        if leftPos < 0:
            leftPos = 0

        while rightPos < len(nums) and nums[rightPos] == nums[targetIndex]:
            rightPos += 1

        while leftPos > -1 and nums[leftPos] == nums[targetIndex]:
            leftPos -= 1

        return [leftPos + 1, rightPos - 1]

    def binary_search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = int((right + left) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        return None


solution = Solution()
answer = solution.searchRange([5, 7, 7, 8, 8, 10], 8)
print(answer)
assert answer == [3, 4]

answer = solution.searchRange([5, 7, 7, 8, 8, 10], 6)
print(answer)
assert answer == [-1, -1]

answer = solution.searchRange([], 0)
print(answer)
assert answer == [-1, -1]

answer = solution.searchRange([1], 1)
print(answer)
assert answer == [0, 0]
