import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1 = "".join(re.findall(r"[a-zA-Z0-9]", s))
        str2 = str1[::-1]

        return str1.lower() == str2.lower()


solution = Solution()
answer = solution.isPalindrome("A man, a plan, a canal: Panama")
print(answer)
assert answer == True
