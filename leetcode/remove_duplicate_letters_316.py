class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        last_occurence = {v: i for i, v in enumerate(s)}

        for i, v in enumerate(s):
            if v in seen:
                continue

            while stack and v < stack[-1] and i < last_occurence[stack[-1]]:
                seen.discard(stack.pop())

            stack.append(v)
            seen.add(v)

        return "".join(stack)


solution = Solution()
answer = solution.removeDuplicateLetters("bcabc")
print(answer)
assert answer == "abc"

answer = solution.removeDuplicateLetters("cbacdcbc")
print(answer)
assert answer == "acdb"
