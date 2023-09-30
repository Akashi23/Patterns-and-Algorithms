from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        counter = 0
        sets = set()
        for i in range(len(nums) -1, -1, -1):
            if nums[i] <= k and not nums[i] in sets:
                sets.add(nums[i])
            counter += 1
            if len(sets) == k:
                return counter
            
            
    

solution = Solution()
answer = solution.minOperations([3,1,5,4,2], 2)
print(answer)
assert answer == 4

answer = solution.minOperations([3,2,5,3,1], 3)
print(answer)
assert answer == 4

answer = solution.minOperations([3,1,5,4,2], 5)
print(answer)
assert answer == 5