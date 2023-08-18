class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word_d1 = self.create_dict(word1)
        word_d2 = self.create_dict(word2)

        if len(word1) != len(word2):
            return False

        if len(word_d1) != len(word_d2):
            return False

        value1 = []
        value2 = []
        keys1 = []
        keys2 = []
        for w1, w2 in zip(word_d1, word_d2):
            value1.append(word_d1[w1])
            value2.append(word_d2[w2])
            keys1.append(w1)
            keys2.append(w2)

        value1.sort()
        value2.sort()
        keys1.sort()
        keys2.sort()

        print(keys1, keys2)

        if keys1 != keys2:
            return False

        if value1 == value2:
            return True

        return False

    def create_dict(self, word: str):
        newDict = {}
        for i in word:
            if not newDict.get(i):
                newDict[i] = 0
            newDict[i] += 1
        return newDict


solution = Solution()
answer = solution.closeStrings("abc", "bca")
print(answer)
assert answer == True

answer = solution.closeStrings("a", "aa")
print(answer)
assert answer == False

answer = solution.closeStrings("cabbba", "abbccc")
print(answer)
assert answer == True

answer = solution.closeStrings("cabbba", "aabbss")
print(answer)
assert answer == False

answer = solution.closeStrings("vvaaccc", "bbbaavv")
print(answer)
assert answer == False

answer = solution.closeStrings("uau", "ssx")
print(answer)
assert answer == False
