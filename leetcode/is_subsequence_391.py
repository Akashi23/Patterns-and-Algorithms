class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        queue = []
        string = [*s]

        for i in t:
            if not string:
                break
            if i == string[0]:
                queue.append(i)
                string.pop(0)

        if queue == [*s]:
            return True
        else:
            return False


solution = Solution()
answer = solution.isSubsequence("", "ahbgdc")
print(answer)
