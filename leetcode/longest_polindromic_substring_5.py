class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)

        dp = [[False] * length for _ in range(length)]
        ans = [0, 0]

        for i in range(length):
            dp[i][i] = True

        for i in range(length - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]

        for diff in range(2, length):
            for i in range(length - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans = [i, j]

        return s[ans[0] : ans[1] + 1]


solution = Solution()
answer = solution.longestPalindrome("babad")
print(answer)
assert answer == "bab" or answer == "aba"

answer = solution.longestPalindrome("cbbd")
print(answer)
assert answer == "bb"

answer = solution.longestPalindrome("a")
print(answer)
assert answer == "a"

answer = solution.longestPalindrome("ac")
print(answer)
assert answer == "a"

answer = solution.longestPalindrome("bb")
print(answer)
assert answer == "bb"

answer = solution.longestPalindrome("ccc")
print(answer)
assert answer == "ccc"
