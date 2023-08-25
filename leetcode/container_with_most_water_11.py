from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_i = 0
        m_i = 0
        m_j = 0
        max_j = 0

        for i in range(len(height)):
            if max_j <= i * height[i]:
                max_j = i * height[i]
                m_j = i

        rev_h = reversed(height)
        for [i, v] in enumerate(rev_h):
            if max_i <= i * v:
                max_i = i * v
                m_i = i
        m_i = len(height) - m_i - 1
        return (m_j - m_i) * min(height[m_i], height[m_j])


solution = Solution()
answer = solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(answer)
assert answer == 49

answer = solution.maxArea([1, 1])
print(answer)
assert answer == 1

answer = solution.maxArea([4, 3, 2, 1, 4])
print(answer)
assert answer == 16

answer = solution.maxArea([1, 2, 1])
print(answer)
assert answer == 2
