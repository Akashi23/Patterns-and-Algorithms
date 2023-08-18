from typing import List


class Solution:
    def decodeString(self, s: str) -> str:
        i, j = 0, len(s) - 1
        stack = []
        s: List[str] = [*s]

        return stack


solution = Solution()
answer = solution.decodeString("3[a]2[bc]")
print(answer)  # "aaabcbc"
assert answer == "aaabcbc"

answer = solution.decodeString("3[a2[c]]")
print(answer)  # "accaccacc"
assert answer == "accaccacc"
