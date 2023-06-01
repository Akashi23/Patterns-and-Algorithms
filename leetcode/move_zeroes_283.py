from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        length = len(nums)
        while j < length:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                i -= 1
            j += 1
            i += 1

        return nums


solution = Solution()
answer = solution.moveZeroes([0, 1, 0, 3, 12])
print(answer)
