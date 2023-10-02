class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        length = 0
        i = 0

        while length < k:
            length = length * int(s[i]) if s[i].isdigit() else length + 1
            i += 1

        for j in range(i - 1, -1, -1):
            if s[j].isdigit():
                length //= int(s[j])
                k %= length
            else:
                if k == 0 or k == length:
                    return s[j]
                length -= 1


solution = Solution()
answer = solution.decodeAtIndex("leet2code3", 10)
print(answer)
assert answer == "o"

answer = solution.decodeAtIndex("ha22", 5)
print(answer)
assert answer == "h"

answer = solution.decodeAtIndex("a2345678999999999999999", 1)
print(answer)
assert answer == "a"


class Solution2:
    def decodeAtIndex(self, s: str, k: int) -> str:
        stack = []
        length = len(s)

        for i in range(length):
            if s[i].isalpha():
                stack.append(s[i])
            if s[i].isdigit():
                if len(stack) > k:
                    return stack[k - 1]
                stack = stack * int(s[i])

        return stack[k - 1]
