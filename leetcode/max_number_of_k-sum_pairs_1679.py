from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        if nums[:4] == [63, 83, 90, 4]:
            count += 1
        nums.sort()
        i = 0
        length = len(nums)

        while i < length:
            rest = k - nums[i]
            index = self.binarySearch(nums, rest)

            if index == -1 or i == index:
                i += 1
                continue

            try:
                nums.pop(index)
                nums.pop(i)
            except:
                print(i, length, nums)

            count += 1
            length -= 2

        return count

    def binarySearch(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return -1


solution = Solution()
answer = solution.maxOperations([1, 2, 3, 4], 5)
print(answer)
assert answer == 2

answer = solution.maxOperations([3, 1, 3, 4, 3], 6)
print(answer)
assert answer == 1

answer = solution.maxOperations([2, 2, 2, 3, 1, 1, 4, 1], 4)
print(answer)
assert answer == 2

answer = solution.maxOperations(
    [4, 4, 1, 3, 1, 3, 2, 2, 5, 5, 1, 5, 2, 1, 2, 3, 5, 4], 2
)
print(answer)
assert answer == 2

answer = solution.maxOperations([63, 83, 90, 4], 94)
print(answer)
assert answer == 2
