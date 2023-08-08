from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot_index = self.binary_min_in_mid_search(nums)
        nums1 = nums[pivot_index:] + nums[:pivot_index]
        result = self.binary_search(nums1, target)
        if result != -1 and nums[-1] >= target:
            result = result + pivot_index
        elif result != -1 and nums[-1] <= target:
            result = result - pivot_index
        return result

    def binary_min_in_mid_search(self, nums: List[int]) -> int:
        left, mid, right = 0, len(nums) // 2, len(nums) - 1
        while nums[left] > nums[right]:
            mid = int((right + left) / 2)
            print(nums[left], nums[mid], nums[right])
            print(left, mid, right)
            if nums[mid - 1] >= nums[mid] < nums[mid + 1]:
                return mid
            elif nums[mid] > nums[left]:
                left = mid - 1
            elif nums[mid] < nums[right]:
                right = mid + 1
                print("right", right)
            if len(nums) == 2:
                return 1
        return 0

    def binary_search(self, nums: List[int], target: int) -> int:
        left, mid, right = 0, len(nums) // 2, len(nums) - 1
        while left <= right:
            mid = int((right + left) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            if len(nums) == 2:
                if target == nums[0]:
                    return 0
                elif target == nums[1]:
                    return 1
                else:
                    return -1
        return -1


solution = Solution()
# answer = solution.search([6, 7, 0, 1, 2, 3, 4, 5], 0)
# print(answer)
# assert answer == 2

# answer = solution.search([4, 5, 6, 7, 0, 1, 2], 3)
# print(answer)
# assert answer == -1

# answer = solution.search([1], 1)
# print(answer)
# assert answer == 0

# answer = solution.search([3, 1], 1)
# print(answer)
# assert answer == 1

# answer = solution.search([5, 1, 3], 5)
# print(answer)
# assert answer == 0

# answer = solution.search([3, 1], 3)
# print(answer)
# assert answer == 0

answer = solution.search([3, 5, 1], 3)
print(answer)
assert answer == 0
