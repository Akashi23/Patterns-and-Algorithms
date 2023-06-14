from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashtable = {}

        for i in nums:
            if not hashtable.get(i):
                hashtable[i] = 1
                continue
            hashtable[i] += 1

        maxi = 0
        maxi_key = 0
        for key in hashtable:
            if hashtable[key] > maxi:
                maxi = hashtable[key]
                maxi_key = key

        return maxi_key


solution = Solution()
answer = solution.majorityElement([3, 2, 3])
print(answer)
assert answer == 3

answer = solution.majorityElement([3, 3, 4])
print(answer)
assert answer == 3
