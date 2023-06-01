class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dict = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M',
        }

        string = str(num)
        length = len(string)
        result = ''

        for i in range(length):
            digit = int(string[i])
            if digit == 0:
                continue
            if digit == 1 or digit == 4 or digit == 5 or digit == 9:
                result += roman_dict[digit * pow(10, length - i - 1)]
                continue
            if digit < 4:
                result += roman_dict[pow(10, length - i - 1)] * digit
                continue
            if digit > 5 and digit < 9:
                result += roman_dict[5 * pow(10, length - i - 1)]
                result += roman_dict[pow(10, length - i - 1)] * (digit - 5)
                continue

        return result


solution = Solution()
answer = solution.intToRoman(1994)
print(answer)
