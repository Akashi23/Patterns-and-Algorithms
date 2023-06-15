from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right_sum = sum(nums[1:])
        left_sum = 0

        for i in range(len(nums) - 1):
            if left_sum == right_sum:
                return i
            
            left_sum += nums[i]
            right_sum -= nums[i + 1]
            print(f"left_sum: {left_sum}, right_sum: {right_sum}")

        if len(nums) == 1:
             return 0

        if left_sum == right_sum:
                return i + 1
        
        return -1
    


solution = Solution()
answer = solution.pivotIndex([1, 7, 3, 6, 5, 6])
print(answer)
assert answer == 3

answer = solution.pivotIndex([1, 2, 3])
print(answer)
assert answer == -1


answer = solution.pivotIndex([2, 1, -1])
print(answer)
assert answer == 0

answer = solution.pivotIndex([-1,-1,0,1,1,0])
print(answer)
assert answer == 5