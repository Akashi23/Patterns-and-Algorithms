from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        current_min = nums[0]
        stack = [(current_min, current_min)]

        for i in nums[1:]:
            while stack and i >= stack[-1][1]:
                stack.pop()
            
            if stack and i > stack[-1][0]:
                return True
            
            stack.append((current_min, i))

            current_min = min(current_min, i)

        return False


solution = Solution()
answer = solution.find132pattern([1,2,3,4])
print(answer)
assert answer == False

answer = solution.find132pattern([3,1,4,2])
print(answer)
assert answer == True

answer = solution.find132pattern([-1,3,2,0])
print(answer)
assert answer == True