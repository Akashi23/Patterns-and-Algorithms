class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        max_vowels = 0
        current_vowels = 0

        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1
                max_vowels += 1
        
        i = 1
        j = k
        length = len(s)

        while j < length:
            if s[i - 1] in vowels:
                current_vowels -= 1
            if s[j] in vowels:
                current_vowels += 1
                if current_vowels > max_vowels:
                    max_vowels = current_vowels
            i += 1
            j += 1

        return max_vowels

solution = Solution()
answer = solution.maxVowels("abciiidef", 3)
print(answer)
assert answer == 3

answer = solution.maxVowels("aeiou", 2)
print(answer)
assert answer == 2

answer = solution.maxVowels("leetcode", 3)
print(answer)
assert answer == 2