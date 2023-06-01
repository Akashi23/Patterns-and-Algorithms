from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, value in enumerate(nums):
            hashmap[value - target] = index

        print(hashmap)
        for index, value in enumerate(nums):
            if -value in hashmap and hashmap[-value] != index:
                return [hashmap[-value], index]
        
        return
        




sol = Solution()
answer = sol.twoSum([3,2,4], 6)
print(answer)