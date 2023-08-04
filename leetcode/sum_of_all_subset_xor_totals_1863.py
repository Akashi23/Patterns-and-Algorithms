from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        summas = 0
        for i in range(2 ** len(nums)):
            summa = 0
            for j in range(len(nums)):
                print("bitwise and", i & (1 << j), i, j, "1 << j ", (1 << j))
                if i & (1 << j):
                    summa ^= nums[j]
            summas += summa
        return summas


solution = Solution()
answer = solution.subsetXORSum([1, 3])
print(answer)
assert answer == 6

answer = solution.subsetXORSum([1, 1, 1])
print(answer)
assert answer == 4
