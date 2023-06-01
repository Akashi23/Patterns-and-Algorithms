from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                for k in range(j, len(nums)):
                    if nums[i] < nums[j] < nums[k]:
                        return True
                if nums[j] >= nums[k]:
                    return False
            if nums[i] >= nums[j]:
                return False
        return False


solution = Solution()
answer = solution.increasingTriplet([1, 2, 3, 4, 5])
print(answer)

assert answer == True
