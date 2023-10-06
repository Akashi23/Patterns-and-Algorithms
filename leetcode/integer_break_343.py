from typing import List


class Solution:
    def integerBreak(self, n: int) -> int:
        s = n
        count = 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        while s != 0 and s != 4 and s != 2:
            s -= 3
            count += 1
        
        if s == 0:
            s = 1
        for i in range(count):
            s *= 3

        return s
        
    def sumBreak(self, n: int) -> List[int]:
        pass


solution = Solution()
answer = solution.integerBreak(2)
print(answer)
assert answer == 1

answer = solution.integerBreak(10)
print(answer)
assert answer == 36