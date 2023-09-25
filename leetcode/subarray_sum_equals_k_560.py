from collections import defaultdict
from typing import List


class Solution:  # O(n)
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSum = 0
        result = 0
        counter = defaultdict(int)

        for num in nums:
            preSum += num

            if preSum == k:
                result += 1

            if preSum - k in counter:
                result += counter[preSum - k]

            counter[preSum] += 1

        return result


class Solution2:  # O(n^2)
    def subarraySum(self, nums: List[int], k: int) -> int:
        dictionary = {}
        count = 0
        summa = 0

        dictionary[0] = 0
        for i, v in enumerate(nums):
            summa += v
            dictionary[i + 1] = summa

        for j in range(0, len(nums) + 1):
            for i in range(j + 1):
                if j == i:
                    continue
                if dictionary[j] - k == dictionary[i]:
                    print(f"i: {i}, j: {j}")
                    count += 1

        return count


solution = Solution()
answer = solution.subarraySum([1, 1, 1], 2)
print(answer)
assert answer == 2

answer = solution.subarraySum([1, 2, 3], 3)
print(answer)
assert answer == 2

answer = solution.subarraySum([1], 1)
print(answer)
assert answer == 1

answer = solution.subarraySum([1], 0)
print(answer)
assert answer == 0

answer = solution.subarraySum([-1, -1, 1], 0)
print(answer)
assert answer == 1
