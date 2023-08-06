from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mappings = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        arrays = []
        digits = [*digits]

        def recursive(digits: List[str], array: List[str]):
            if not digits:
                return array

            digit = digits.pop(0)
            if not array:
                array.extend(mappings[digit])
                return recursive(digits, array)
            
            new_array = []
            for j in array:
                new_a = []
                for i in mappings[digit]:
                    new_a.append(j+i)
                new_array.extend(new_a)

            return recursive(digits, new_array)
       
        arrays = recursive(digits, arrays)
        return arrays

            


solution = Solution()
answer = solution.letterCombinations("23")
print(answer)
assert answer == ["ad","ae","af","bd","be","bf","cd","ce","cf"]

answer = solution.letterCombinations("")
print(answer)
assert answer == []

answer = solution.letterCombinations("2")
print(answer)
assert answer == ["a","b","c"]