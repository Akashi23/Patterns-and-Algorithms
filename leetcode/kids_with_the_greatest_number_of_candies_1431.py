from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []

        for i in candies:
            result.append(self.max_element(i + extraCandies, candies))

        return result

    def max_element(self, elem: int, arr: List[int]) -> bool:
        for i in arr:
            if elem < i:
                return False

        return True


solution = Solution()
answer = solution.kidsWithCandies([2, 3, 5, 1, 3], 3)
print(answer)
