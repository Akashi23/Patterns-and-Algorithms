from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        factorials = [1, 2, 6, 24, 120, 720]

        length = factorials[len(nums) - 1]

        result = []

        for _ in range(length):
            permutes = []
            for num in nums:
                permutes.append(num)
            result.append(permutes)
        return result
    
    def generate(self, )


solution = Solution()
answer = solution.permute([1, 2, 3])
print(answer)
assert answer == [[1, 2, 3], [1, 3, 2], [
    2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
