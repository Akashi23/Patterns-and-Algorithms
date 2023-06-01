class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        queue = []
        string = [*s]

        for i in string:
            if i in vowels:
                queue.append(i)

        for i in range(len(string)):
            if string[i] in vowels:
                string[i] = queue.pop()

        return ''.join(string)


solution = Solution()
answer = solution.reverseVowels("hello")
print(answer)
