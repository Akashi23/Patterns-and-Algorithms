from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = {}
        columns = {}

        for i in grid:
            string = ""
            for j in i:
                string += f"{j},"
            if not rows.get(string):
                rows[string] = 0
            rows[string] += 1

        for i in range(len(grid)):
            string = ""
            for j in range(len(grid)):
                string += f"{grid[j][i]},"
            if not columns.get(string):
                columns[string] = 0
            columns[string] += 1

        number = 0
        for i in rows:
            if columns.get(i):
                number += rows[i] * columns[i]

        return number

    def print_grid(self, grid: List[List[int]]):
        for i in grid:
            print(i)


solution = Solution()
answer = solution.equalPairs([[13, 13], [13, 13]])
print(answer)
assert answer == 4

answer = solution.equalPairs([[11, 1], [1, 11]])
print(answer)
assert answer == 2

answer = solution.equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]])
print(answer)
assert answer == 1

answer = solution.equalPairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]])
print(answer)
assert answer == 3

answer = solution.equalPairs([[2, 1, 1, 7], [1, 1, 1, 1], [23, 1, 5, 1], [2, 12, 3, 2]])
print(answer)
assert answer == 0
