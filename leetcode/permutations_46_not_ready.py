from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        all_permutations = []
        for i in range(2 ** len(nums)):
            permutation = []
            for j in range(len(nums)):
                print("bitwise and", i & (1 << j))

                if i & (1 << j):
                    permutation.append(nums[j])
            summas += summa
        return summas


solution = Solution()
answer = solution.permute([1, 2, 3])
print(answer)
assert answer == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
