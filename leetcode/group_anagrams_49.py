from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        listD = []
        for i in strs:
            length = str(len(i))
            string = "".join(sorted(list(i)))
            joined = length + string

            if joined in dictionary:
                dictionary[joined].append(i)
            else:
                dictionary[joined] = [i]

        for i in dictionary:
            listD.append(dictionary[i])

        return listD


solution = Solution()
answer = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(answer)
assert answer == [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

answer = solution.groupAnagrams([""])
print(answer)
assert answer == [[""]]

answer = solution.groupAnagrams(["a"])
print(answer)
assert answer == [["a"]]
