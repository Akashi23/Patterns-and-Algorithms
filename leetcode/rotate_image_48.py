from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        length = len(matrix)

        for i in range(length):
            matrix.append([])
            print(matrix)
            print(length + (length - i))
            for j in range(length - 1, -1, -1):
                matrix[length + i].append(matrix[j][i])

        for i in range(length):
            matrix.pop(0)

        return matrix


solution = Solution()
answer = solution.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(answer)
assert answer == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
