from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 1
        length = len(chars)
        counter = 1
        char = chars[0]

        while i < length:
            if char == chars[i]:
                counter += 1
            else:
                if counter > 1:
                    chars.append(char)
                    for j in range(len(str(counter))):
                        chars.append(str(counter)[j])
                else:
                    chars.append(char)
                counter = 1
                char = chars[i]
            i += 1

        if counter > 1:
            chars.append(char)
            for j in range(len(str(counter))):
                chars.append(str(counter)[j])
        else:
            chars.append(char)

        for i in range(length):
            chars.pop(0)

        print(chars)

        return len(chars)


solution = Solution()
answer = solution.compress(["a", "a", "b", "b", "c", "c", "c"])
print(answer)
assert answer == 6

answer = solution.compress(["a"])
print(answer)
assert answer == 1

answer = solution.compress(
    ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
)
print(answer)
assert answer == 4
