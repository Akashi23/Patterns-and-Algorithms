from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.backtrack(candidates, target, [], result)
        return result

    def backtrack(self, candidates: List[int], target: int, path: List[int], result: List[List[int]]):
        if target == 0:
            result.append(path)
            return
        if target < 0:
            return
        for i in range(len(candidates)):
            self.backtrack(
                candidates[i:], target-candidates[i], path + [candidates[i]], result)


solution = Solution()
answer = solution.combinationSum([2, 3, 6, 7], 7)
print(answer)
