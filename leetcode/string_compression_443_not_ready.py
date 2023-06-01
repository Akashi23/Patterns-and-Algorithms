from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        length = len(chars)
        counter = 1

        while i < length:
            print(chars)
            if chars[-1] != chars[i]:
                chars.append(chars[i])
                if counter > 1:
                    chars.append(str(counter + 1))
            else:
                counter += 1
            i += 1
        return chars


solution = Solution()
answer = solution.compress(["a", "a", "b", "b", "c", "c", "c"])
print(answer)
