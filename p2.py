def roman_to_decimal(str1):
    # your statement follows
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
    n = 0
    stack = list()
    count = len(str1)
    for x in str1:
        stack.append(rom_val[x])
    prev = 0
    while len(stack) > 0:
        current = stack.pop()
        if prev > current:
            n -= current
            prev = current
            continue
        n += current
        prev = current

    return n

def decimal_to_roman(n):
    # your statement follows
    int_val={0:["","I","II","III","IV","V","VI","VII","VIII","IX"], 1:["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"],}
    str1 = ''
    str1 += int_val[1][int((n - n % 10) / 10)]
    str1 += int_val[0][n % 10]

    return str1

if __name__ == '__main__':
    # you can test your function by using the following
    print(roman_to_decimal('XII'))
    print(decimal_to_roman(7))


