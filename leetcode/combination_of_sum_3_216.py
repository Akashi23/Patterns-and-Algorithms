from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(nums: List[int], k_num: int, target: int, m_num: int, result: List[List[int]]) -> List[List[int]]:
            if k_num == 0 and target == 0:
                result.append(sorted(nums))
                return
            
            if target <= 0:
                return
            
            print(nums, k_num, target, m_num)
            for i in range(1, m_num):
                if target - i >= 0:
                    backtrack(nums + [i], k_num - 1, target - i, i, result)
        result = []
        backtrack([], k, n, 10, result)
        return result

        
        

solution = Solution()
# answer = solution.combinationSum3(3, 7)
# print(answer)
# assert answer == [[1, 2, 4]]

answer = solution.combinationSum3(9, 45)
print(answer)
assert answer == [[1, 2, 3, 4, 5, 6, 7, 8, 9]]