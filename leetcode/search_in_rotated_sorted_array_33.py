from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot_index = self.binary_min_in_mid_search(nums)
        result = self.binary_search(nums, target, pivot_index, len(nums) - 1)
        if result == -1:
            result = self.binary_search(nums, target, 0, pivot_index)

        return result

    def binary_min_in_mid_search(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        value = nums[-1]
        while left <= right:
            mid = int((right + left) / 2)
            if value < nums[mid]:
                left = mid + 1
            elif value >= nums[mid]:
                right = mid - 1
        return left

    def binary_search(self, nums: List[int], target: int, low: int, high: int) -> int:
        left, right = low, high
        while left <= right:
            mid = int((right + left) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        return -1


solution = Solution()
answer = solution.search([6, 7, 0, 1, 2, 3, 4, 5], 0)
print(answer)
assert answer == 2

answer = solution.search([4, 5, 6, 7, 0, 1, 2], 0)
print(answer)
assert answer == 4

answer = solution.search([4, 5, 6, 7, 0, 1, 2], 3)
print(answer)
assert answer == -1

answer = solution.search([1], 1)
print(answer)
assert answer == 0

answer = solution.search([3, 1], 1)
print(answer)
assert answer == 1

answer = solution.search([5, 1, 3], 5)
print(answer)
assert answer == 0

answer = solution.search([3, 1], 3)
print(answer)
assert answer == 0

answer = solution.search([3, 5, 1], 3)
print(answer)
assert answer == 0
