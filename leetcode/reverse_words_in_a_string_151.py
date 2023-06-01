import re


class Solution:
    def reverseWords(self, s: str) -> str:
        words = re.findall("\w+", s)
        words.reverse()
        return ' '.join(words)


solution = Solution()
answer = solution.reverseWords("the  sky is blue")
print(answer)
