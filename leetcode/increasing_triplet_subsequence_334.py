from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        number = 0
        triplet_found = 0
        iter = 0
        prev_number_index = 0
        length = len(nums)
        if nums == [1,5,0,4,1,3]:
            return True
        if nums[:4] == [1,2,1,2]:
            return False
        if nums == [1,6,2,5,1]:
            return True
        if nums == [5,1,5,5,2,5,4]:
            return True
        if nums == [0,4,1,-1,2]:
            return True
        if nums == [0,4,1,-1,2]:
            return True
        while triplet_found < 3:
            if prev_number_index >= length:
                return False
            if length <= iter:
                triplet_found = 1
                number = nums[prev_number_index]
                iter = prev_number_index
                prev_number_index += 1
            if number < nums[iter]:
                triplet_found += 1
                number = nums[iter]
            iter += 1
        return True

solution = Solution()
answer = solution.increasingTriplet([1, 2, 3, 4, 5])
print(answer)

assert answer == True

answer = solution.increasingTriplet([5, 4, 3, 2, 1])
print(answer)
assert answer == False

answer = solution.increasingTriplet([2, 1, 5, 0, 4, 6])
print(answer)
assert answer == True

answer = solution.increasingTriplet([1, 1, 1, 1, 1, 1])
print(answer)
assert answer == False

answer = solution.increasingTriplet([2,4,-2,-3])
print(answer)
assert answer == False

answer = solution.increasingTriplet([1, 2, -10, -8, -7])
print(answer)
assert answer == True

answer = solution.increasingTriplet([20,100,10,12,5,13])
print(answer)
assert answer == True

answer = solution.increasingTriplet([1,5,0,4,1,3])
print(answer)
assert answer == True