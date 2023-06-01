from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(numbers)):
            if numbers[i] in d:
                return [d[numbers[i]], i+1]
            else:
                d[target - numbers[i]] = i+1


solution = Solution()
answer = solution.twoSum([1, 2, 3, 4, 4, 9, 56, 90], 8)
print(answer)
assert answer == [4, 5]
