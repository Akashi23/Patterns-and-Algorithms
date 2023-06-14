from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum = 0
        for i in range(len(gain)):
            prefix_sum += gain[i]
            gain[i] = prefix_sum
        gain.append(0)
        return max(gain)


solution = Solution()
answer = solution.largestAltitude([-5, 1, 5, 0, -7])
print(answer)
assert answer == 1

answer = solution.largestAltitude([-4, -3, -2, -1, 4, 3, 2])
print(answer)
assert answer == 0