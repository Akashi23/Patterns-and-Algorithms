from typing import List


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(len(self.rectangle)):
            for j in range(len(self.rectangle[i])):
                if row1 <= i <= row2 and col1 <= j <= col2:
                    self.rectangle[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]

        # Your SubrectangleQueries object will be instantiated and called as such:
        # obj = SubrectangleQueries(rectangle)
        # obj.updateSubrectangle(row1,col1,row2,col2,newValue)
        # param_2 = obj.getValue(row,col)


solution = SubrectangleQueries([[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]])
solution.updateSubrectangle(0, 0, 3, 2, 5)
print(solution.getValue(0, 2))
print(solution.getValue(3, 1))
solution.updateSubrectangle(3, 0, 3, 2, 10)
print(solution.getValue(3, 1))
print(solution.getValue(0, 2))
