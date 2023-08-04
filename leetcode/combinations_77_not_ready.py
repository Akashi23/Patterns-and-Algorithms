from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:



solution = Solution()
answer = solution.combine(4, 2)
print(answer)
assert answer == [[2, 4], [3, 4], [2, 3], [1, 2], [1, 3], [1, 4]]
