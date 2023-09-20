from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]
        stack = [len(temperatures) - 1]

        for i in range(len(temperatures) - 2, -1, -1):
            while len(stack) > 0 and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if not stack:
                answer.append(0)
            else:
                answer.append(stack[-1] - i)

            stack.append(i)

        answer.reverse()    
        return answer
    
 
solution = Solution()
answer = solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
print(answer)
assert answer == [1, 1, 4, 2, 1, 1, 0, 0]

answer = solution.dailyTemperatures([30, 40, 50, 60])
print(answer)
assert answer == [1, 1, 1, 0]

answer = solution.dailyTemperatures([30, 60, 90])
print(answer)
assert answer == [1, 1, 0]

answer = solution.dailyTemperatures([30, 30, 30])
print(answer)
assert answer == [0, 0, 0]


class Solution2:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = []

        length =  len(temperatures)
        i = 0
        while i < length:
            j = i
            count = 0
            while j < length - 1:
                count += 1
                if temperatures[i] < temperatures[j + 1]:
                    answer.append(count)
                    break
                j += 1
            if j == length - 1 and j - i ==  count:
                answer.append(0)
            i += 1

        return answer
    