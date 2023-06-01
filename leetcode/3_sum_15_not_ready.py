from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                print('threesum = ', nums[i], nums[j], -(nums[i] + nums[j]))
                thirdNumber = self.binarySearch(nums, -(nums[i] + nums[j]))
                if thirdNumber:
                    print(nums[thirdNumber])
                    o = sorted([nums[i], nums[j], nums[thirdNumber]])
                    if o not in result:
                        result.append(o)
        return result

    def binarySearch(self, nums: List[int], target: int) -> bool:
        left, middle, right = 0, round(len(nums)/2), len(nums)
        print('search = ', target)
        while (right != left):
            if (nums[middle] < target):
                right = middle
                middle = round((right - left) / 2)
            elif (nums[middle] > target):
                left = middle
                middle = round((right - left) / 2)
        if nums[middle] == target:
            return middle
        return None


solution = Solution()
answer = solution.threeSum([-1, 0, 1, 2, -1, -4])
print(answer)
assert answer == [[-1, -1, 2], [-1, 0, 1]]
