from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, middle, right = 0, round(len(nums)/2), len(nums)
        while(right != left):
            if(nums[middle] < target):
                right = middle
                middle = round((right - left) / 2)
            elif(nums[middle] > target):
                left = middle
                middle = round((right - left) / 2)
        
        print(nums[middle])
        if nums[middle] == target:
            return middle
        return -1


sol = Solution()
answer = sol.search([-1,0,3,5,9,12], 9)
print(answer)