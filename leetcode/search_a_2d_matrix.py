from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        array_vertical = [matrix[i][0] for i in range(len(matrix))]
        index = self.findClosest(array_vertical, len(array_vertical), target)
        if self.binarySearch(matrix[index], target) != -1:
            return True
        return False

    def findClosest(self, arr, n, target):
        # Corner cases
        if target <= arr[0]:
            return 0
        if target >= arr[n - 1]:
            return n - 1

        # Doing binary search
        i = 0
        j = n
        mid = 0
        while i < j:
            mid = (i + j) // 2

            if arr[mid] == target:
                return mid

            # If target is less than array
            # element, then search in left
            if target < arr[mid]:
                # If target is greater than previous
                # to mid, return closest of two
                if mid > 0 and target > arr[mid - 1]:
                    return self.getClosest(arr, mid - 1, mid, target)

                # Repeat for left half
                j = mid

            # If target is greater than mid
            else:
                if mid < n - 1 and target < arr[mid + 1]:
                    return self.getClosest(arr, mid, mid + 1, target)

                # update i
                i = mid + 1

        # Only single element left after search
        return mid

    def getClosest(self, arr, val1, val2, target):
        if target - arr[val1] > 0:
            return val1
        else:
            return val2

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
answer = solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 34)
print(answer)
assert answer == True

answer = solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 7)
print(answer)
assert answer == True

answer = solution.searchMatrix([[1]], 0)
print(answer)
assert answer == False

answer = solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
print(answer)
assert answer == True

solution = Solution()
answer = solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20]], 13)
print(answer)
assert answer == False
