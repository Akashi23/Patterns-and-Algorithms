from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        length = len(nums)
        while i < length:
            if not nums[i] & 1:
                nums.insert(0, nums[i])
                del nums[i + 1]

            i += 1
        return nums


solution = Solution()
answer = solution.sortArrayByParity([3, 1, 2, 4])
print(answer)
assert answer == [4, 2, 1, 3]

answer = solution.sortArrayByParity([0])
print(answer)
assert answer == [0]

answer = solution.sortArrayByParity([1])
print(answer)
assert answer == [1]
