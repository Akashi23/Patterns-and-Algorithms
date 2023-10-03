class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        A = []
        B = []

        countA = 0
        countB = 0

        for i in colors:
            if i == "A":
                countA += 1
                if countB > 2:
                    B.append(countB)
                countB = 0
            if i == "B":
                countB += 1
                if countA > 2:
                    A.append(countA)
                countA = 0

        if i == "B" and countB > 2:
            B.append(countB)

        if i == "A" and countA > 2:
            A.append(countA)

        countA = 0
        countB = 0

        for i in A:
            countA += i - 2

        for i in B:
            countB += i - 2

        if countA < 1:
            return False

        if countB >= countA:
            return False
        else:
            return True


solution = Solution()
answer = solution.winnerOfGame("AAABABB")
print(answer)
assert answer == True

answer = solution.winnerOfGame("AA")
print(answer)
assert answer == False

answer = solution.winnerOfGame("ABBBBBBBAAA")
print(answer)
assert answer == False

answer = solution.winnerOfGame("AAAABBBB")
print(answer)
assert answer == False

answer = solution.winnerOfGame("AAAAABBBBBBAAAAA")
print(answer)
assert answer == True
