from bisect import bisect_left
from typing import Dict, List


class Solution:
    def minDeletions(self, s: str) -> int:
        d: Dict[str, int] = {}
        for i in s:
            if i not in d:
                d[i] = 0
            d[i] += 1
            
        values = d.values()  
        duplicates = self.findDuplicates(values)
        
        for i in duplicates:
            

    def findDuplicates(self, nums: List[int]) -> List[int]:
        dupl = []
        seen = set()
        for num in nums:
            if num in seen:
                dupl.append(num)
            seen.add(num)
        return dupl


solution = Solution()
answer = solution.minDeletions("aab")
print(answer)
assert answer == 0

answer = solution.minDeletions("aaabbbcc")
print(answer)
assert answer == 2

answer = solution.minDeletions("ceabaacb")
print(answer)
assert answer == 2

answer = solution.minDeletions("bbcebab")
print(answer)
assert answer == 2

answer = solution.minDeletions("accdcdadddbaadbc")
print(answer)
assert answer == 1
