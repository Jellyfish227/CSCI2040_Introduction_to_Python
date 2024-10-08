def divisible_sublist(list1, d1, d2):
    # your statement follows
    lista = list(filter(lambda x: (x % d1 == 0) | (x % d2 == 0), list1))
    listb = list(filter(lambda x: (x % d1 == 0) & (x % d2 == 0), list1))
    listc = list(filter(lambda x: (x % d1 != 0) & (x % d2 != 0), list1))
    return lista, listb, listc


if __name__ == '__main__':
    # you can test your function by using the following
    list1 = [21, 25, 9, 16, 28]
    d1 = 3
    d2 = 7
    print(divisible_sublist(list1, d1, d2))
