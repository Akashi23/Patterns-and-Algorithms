class Solution:
    def longestPalindrome(self, s: str) -> str:
        





class Solution2:
    def longestPalindrome(self, s: str) -> str:
        long_polindrome = [[x] for x in s]
        for index, value in enumerate(s):
            for jndex in range(len(s) // 2 + 1):
                if(self.polindrome(s[index - jndex:index + jndex + 1]) and index - jndex > -1):
                    long_polindrome[index].append(s[index - jndex:index + jndex + 1])
                if(self.polindrome(s[index - jndex:index + jndex + 2]) and index - jndex > -1):
                    long_polindrome[index].append(s[index - jndex:index + jndex + 2])
                    
        return self.find_max_polindrome(long_polindrome)
        
    def polindrome(self, s: str) -> bool:
        return s == s[::-1]
    
    def find_max_polindrome(self, lists):
        polindromes = [x.pop() for x in lists]
        return max(polindromes, key=len)
    

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