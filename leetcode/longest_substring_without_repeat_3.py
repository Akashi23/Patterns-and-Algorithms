class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ''
        substring = []
        for i in range(len(s)):
            if s[i] in substring:
                substring.pop(s.index(s[i]))
                print(s[i])
            if s[i] not in substring:
                substring.append(s[i])
                if len(longest) < len(substring):
                    longest = ''.join(substring)
            print(longest, substring)
        return len(longest)

        
            

sol = Solution()
answer = sol.lengthOfLongestSubstring("abcabcdd")
print(answer)