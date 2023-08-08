"""
Даны два массива: [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
Надо вернуть [1, 2, 2, 3] (порядок неважен)
"""

list1 = [1, 2, 3, 2, 0]
list2 = [5, 1, 2, 7, 3, 2]


# n^2
def commons(a, b):
    c = []
    for i in a:
        for j in b:
            if i == j:
                c.append(j)
                b.remove(j)
                continue

    print(c)


commons([*list1], [*list2])


def common_elements(a, b):
    b_dict = {}  # defaultdict выжил :)
    for el in b:
        if not b_dict.get(el):
            b_dict[el] = 1
        b_dict[el] += 1  # я считаю все элементы из b, т.е. типа collections.Counter

    result = []

    for el in a:
        count = b_dict.get(el)
        if count and count > 0:  # если какой-то элемент из a встречается в b
            result.append(el)  # то это успех
            b_dict[el] -= 1  # и я "вынимаю" его из b, т.е. уменьшаю его количество на 1

    return result


print(common_elements(list1, list2))
