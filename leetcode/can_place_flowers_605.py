from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        can_place_number = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left = (i == 0) or (flowerbed[i - 1] == 0) 
                right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0) 

                if left and right:
                    can_place_number += 1
                    flowerbed[i] = 1
        
        return can_place_number >= n


solution = Solution()
answer = solution.canPlaceFlowers([1, 0, 0, 0, 1], 1)
print(answer)
assert answer == True

answer = solution.canPlaceFlowers([1, 0, 0, 0, 1], 2)
print(answer)
assert answer == False

answer = solution.canPlaceFlowers([1, 0, 0, 0, 0, 1], 2)
print(answer)
assert answer == False

answer = solution.canPlaceFlowers([1, 0, 0, 0, 0, 0, 1], 2)
print(answer)
assert answer == True

answer = solution.canPlaceFlowers([0, 0, 1, 0, 1], 1)
print(answer)
assert answer == True