from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        newarr = []
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m * n):
            
                


solution = Solution()
answer = solution.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(answer)
assert answer == [1, 2, 3, 6, 9, 8, 7, 4, 5]

answer = solution.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(answer)
assert answer == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
