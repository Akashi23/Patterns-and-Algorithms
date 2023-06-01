from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        low, high = 0, 1
        length = len(nums) - 1
        if length == 0:
            return 1
        while high != length:
            print(low, high)
            if nums[low] != nums[high]:
                low += 1
                high += 1
            else:
                nums.remove(nums[high])
                length -= 1
                high -= 1
                low -= 1

        return length + 1


solution = Solution()
answer = solution.removeDuplicates([0, 0, 0, 0])
print(answer)
assert answer == 2
