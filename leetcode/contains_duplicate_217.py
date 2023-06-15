from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}

        for i in nums:
            if not i in d:
                d[i] = 0
            d[i] += 1

        for i in d:
            if d[i] > 1:
                return True

        return False


solution = Solution()
answer = solution.containsDuplicate([1, 2, 3, 1])
print(answer)
assert answer == True
