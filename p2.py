# Sample answer
list0 = range(1, 12)
# 2a
list1 = list(map(lambda x: 2 ** x, list0))
list2 = list(map(lambda x: x % 3, list0))

# 2b
list3 = [x for x in range(1, 20) if x % 2 != 0]
list4 = [x for x in range(1, 20) if (x ** 0.5) % 1 == 0]

# 2c
list5 = [0 if (x < 0) else x for x in range(-5, 6)]

# 2d
from functools import reduce
list6 = [reduce(lambda x, y: x * y, range(1, i + 1)) for i in range(1, 12)]

# 2e
student_scores = {
        "Alice": 92,
        "Bob": 85,
        "Charlie": 77,
        "Diana": 88,
        "Ethan": 95,
        "Fiona": 55,
        "George": 68,
        "Hannah": 99,
    }
list7 = [name.upper() for name, score in student_scores.items() if (score > 80)]

# 2f
dict1 = {i: str(' ').join(['{}*{}={}'.format(j, i, i*j) for j in range(1, i + 1)]) for i in range(1, 10)}


# print(list1)
# print(list2)
# print(list3)
# print(list4)
# print(list5)
# print(list6)
# print(list7)
# print(dict1)
