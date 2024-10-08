def recursive_sqrt(a, x):
    # a is an integer, x is the former guess
    # your statement follows
    value = 0.5 * (x + a/x)
    if abs(value - x) > 0.001:
        value = recursive_sqrt(a, value)
    return value # value is next square root guess

if __name__ == '__main__':
    # you can test your function by using the following
    print(recursive_sqrt(2, 1))
