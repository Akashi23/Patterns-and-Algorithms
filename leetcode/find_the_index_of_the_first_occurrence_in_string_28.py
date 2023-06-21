class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_needle = len(needle)
        len_haystack = len(haystack)
        if len_needle > len_haystack:
            return -1

        if len_haystack == len_needle and haystack == needle:
            return 0

        for i in range(len_haystack - len_needle + 1):
            if haystack[i:len_needle+i] == needle:
                return i
            print(haystack[i:len_needle+i], needle)
        return -1


solution = Solution()
answer = solution.strStr("hello", "ll")
print(answer)
assert answer == 2

answer = solution.strStr("abc", "c")
print(answer)
assert answer == 2
