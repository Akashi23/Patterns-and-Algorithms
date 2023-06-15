class Solution:
    def validPalindrome(self, s: str) -> bool:
        incorrect = 0
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                incorrect += 1
                if incorrect > 1:
                    return False
                if s[j] == s[i + 1]:
                    print(s, i, j, s[:i], s[j+1:])
                    s = s[:i] + s[i + 1:]
                    j -= 1

                elif s[i] == s[j-1]:
                    print(s, i, j, s[:i], s[j+1:])
                    s = s[:j] + s[j + 1:]
                    j -= 1

        return True


solution = Solution()
# answer = solution.validPalindrome("abca")
# print(answer)
# assert answer == True


# answer = solution.validPalindrome("deeee")
# print(answer)
# assert answer == True

# answer = solution.validPalindrome("tcaac")
# print(answer)
# assert answer == True

# answer = solution.validPalindrome("aeacdeaeaaaaaaeaedcae")
# print(answer)
# assert answer == True

answer = solution.validPalindrome(
    "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga")
print(answer)
assert answer == True
