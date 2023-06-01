from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        memo = {}

        for i in range(len(nums)):
            if memo.get(nums[i]):
                result.append(memo.get(nums[i]))
                continue
            mul = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                mul *= nums[j]
            memo[nums[i]] = mul
            print(memo[nums[i]])
            result.append(mul)
        return result


solution = Solution()
answer = solution.productExceptSelf([4, 3, 2, 1, 2])
print(answer, [12, 16, 24, 48, 24])

assert answer == [12, 16, 24, 48, 24]
