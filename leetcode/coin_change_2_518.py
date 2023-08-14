from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:



solution = Solution()
answer = solution.change(5, [1, 2, 5])
print(answer)
assert answer == 4, f"Expected 4, got {answer}"

answer = solution.change(3, [2])
print(answer)
assert answer == 0, f"Expected 0, got {answer}"

answer = solution.change(10, [10])
print(answer)
assert answer == 1, f"Expected 1, got {answer}"

answer = solution.change(500, [3, 5, 7, 8, 9, 10, 11])
print(answer)
assert answer == 35502874, f"Expected 35502874, got {answer}"