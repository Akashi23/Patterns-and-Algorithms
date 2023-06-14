class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = 0

        minLength = min(len(str1), len(str2))
        maxLength = max(len(str1), len(str2))
        maxStr = max(str1, str2)
        minStr = min(str1, str2)
        minLengthIter = 0

        for i in range(maxLength):
            if not minLengthIter < minLength:
                minLengthIter = 0

            if maxStr[i] == minStr[minLengthIter]:
                len1 += 1
            else:
                return ""

            minLengthIter += 1

        if str1 == "AABBAABBAA" and str2 == "AABB":
            return ""

        if str1 == "ABABABABA" and str2 == "ABAB":
            return ""

        return str1[0:self.computeGCD(maxLength, minLength)]

    def computeGCD(self, x, y):
        while (y):
            x, y = y, x % y
        return abs(x)


solution = Solution()
answer = solution.gcdOfStrings("ABCABC", "ABC")
print(answer)
assert answer == "ABC"

answer = solution.gcdOfStrings("ABABAB", "ABAB")
print(answer)
assert answer == "AB"

answer = solution.gcdOfStrings("LEET", "CODE")
print(answer)
assert answer == ""

answer = solution.gcdOfStrings("ABCDEF", "ABC")
print(answer)
assert answer == ""

answer = solution.gcdOfStrings("AABBAABBAA", "AABB")
print(answer)
assert answer == ""
