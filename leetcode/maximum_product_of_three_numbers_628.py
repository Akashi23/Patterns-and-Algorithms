from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        self.sort(nums, 0, len(nums) - 1)

        print(nums)

        a = nums[0] * nums[1] * nums[-1]
        b = nums[-1] * nums[-2] * nums[-3]

        return max(a, b)

    def sort(self, arr: List[int], low, high):
        if low < high:
            pi = self.partition(arr, low, high)

            self.sort(arr, low, pi - 1)
            self.sort(arr, pi + 1, high)

    def partition(self, array: List[int], low: int, high: int):
        pivot = array[high]

        i = low - 1

        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]

        array[i+1], array[high] = array[high], array[i+1]
        return i + 1


solution = Solution()
answer = solution.maximumProduct([-1, -2, -3])
print(answer)
assert answer == -6

answer = solution.maximumProduct([-1, -2, 1, 2, 3])
print(answer)
assert answer == 6

answer = solution.maximumProduct([-4, -3, -2, -1, 60])
print(answer)
assert answer == 720

answer = solution.maximumProduct([-710, -107, -851, 657, -14, -859, 278, -182, -749, 718, -640, 127, -930, -462, 694, 969, 143, 309, 904, -651, 160, 451, -159, -316, 844, -60, 611, -169, -73, 721, -902, 338, -20, -890, -819, -644, 107, 404, 150, -219, 459, -324, -385, -118, -307, 993, 202, -
                                 147, 62, -94, -976, -329, 689, 870, 532, -686, 371, -850, -186, 87, 878, 989, -822, -350, -948, -412, 161, -88, -509, 836, -207, -60, 771, 516, -287, -366, -512, 509, 904, -459, 683, -563, -766, -837, -333, 93, 893, 303, 908, 532, -206, 990, 280, 826, -13, 115, -732, 525, -939, -787])
print(answer)
assert answer == 972256230
