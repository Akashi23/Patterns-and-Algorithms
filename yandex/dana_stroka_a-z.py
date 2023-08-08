"""
Дана строка (возможно, пустая), состоящая из букв A-Z: AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28
И сгенерирует ошибку, если на вход пришла невалидная строка.
Пояснения: Если символ встречается 1 раз, он остается без изменений; Если символ повторяется более 1 раза, к нему добавляется количество повторений.
"""


test_string = "AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB"
output_string = "A4B3C2XYZD4E3F3A6B28"


def lre(string: str):
    a_z = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    out = ""
    prev = string[0]
    count = 1
    string = string[1:]
    for i in string:
        if i not in a_z:
            raise ValueError("Is not valid!")
        if prev != i:
            out += prev
            if count > 1:
                out += str(count)
            count = 1
        if prev == i:
            count += 1
        prev = i
    out += prev
    if count > 1:
        out += str(count)
    return out


print(lre(test_string))
assert lre(test_string) == output_string
