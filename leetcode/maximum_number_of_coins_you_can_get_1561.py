from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        maxCoins = 0
        piles.sort(reverse=True)
        i = 0
        while piles:
            if i & 1:
                maxCoins += piles[0]
                piles.pop()
            piles.pop(0)
            i += 1
        return maxCoins


solution = Solution()
answer = solution.maxCoins([2, 4, 1, 2, 7, 8])
print(answer)
assert answer == 9

answer = solution.maxCoins([2, 4, 5])
print(answer)
assert answer == 4

answer = solution.maxCoins([9, 8, 7, 6, 5, 1, 2, 3, 4])
print(answer)
assert answer == 18
