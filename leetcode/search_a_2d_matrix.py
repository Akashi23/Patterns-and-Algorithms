from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:
                if self.binarySearch(matrix[i], target) != -1:
                    return True

        return False

    def binarySearch(self, nums: List[int], target: int) -> bool:
        left, middle, right = 0, round(len(nums)/2), len(nums)
        print(nums)
        while (right != left):
            if (nums[middle] < target):
                right = middle
                middle = round((right - left) / 2)
            elif (nums[middle] > target):
                left = middle
                middle = round((right - left) / 2)
            if nums[middle] == target:
                return middle
        return -1


solution = Solution()
answer = solution.searchMatrix(
    [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 34)
print(answer)
