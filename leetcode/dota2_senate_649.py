class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        pass


solution = Solution()
answer = solution.predictPartyVictory("RD")
print(answer)
assert answer == "Radiant"

answer = solution.predictPartyVictory("RDD")
print(answer)
assert answer == "Dire"

answer = solution.predictPartyVictory("DDRRR")
print(answer)
assert answer == "Dire"
