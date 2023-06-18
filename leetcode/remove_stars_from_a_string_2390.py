class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for i in s:
            if '*' == i:
                if stack:
                    stack.pop()
                continue
            stack.append(i)

        return ''.join(stack)


solution = Solution()
answer = solution.removeStars("ab*c")
print(answer)
assert answer == "ac"