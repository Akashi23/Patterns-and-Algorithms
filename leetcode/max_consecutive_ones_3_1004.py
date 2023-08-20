from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        length = len(nums)
        i, j = 0, 0

        for i in range(length):
            if nums[i] == 0:
                k -= 1

            if k < 0:
                if nums[j] == 0:
                    k += 1
                j += 1
           
        return i - j + 1            

        
    

solution = Solution()
answer = solution.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)
print(answer)
#assert answer == 6

#answer = solution.longestOnes([1,1,1,0,0,0,1,1,1,1], 0)
#print(answer)
#assert answer == 4

#answer = solution.longestOnes([0,0,0,1], 4)
#print(answer)
#assert answer == 4

#answer = solution.longestOnes([0,0,1,1,1,0,0], 0)
#print(answer)
#assert answer == 3

answer = solution.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)
print(answer)
assert answer == 10