from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = {}
        for i in arr:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        uniques = set()

        for i in hashmap:
            uniques.add(hashmap[i])
        
        if len(hashmap) != len(uniques):
            return False
        
        return True


solution = Solution()
answer = solution.uniqueOccurrences([1, 2, 2, 1, 1, 3])
print(answer)
assert answer == True