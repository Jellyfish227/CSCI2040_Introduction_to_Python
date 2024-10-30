def quicksort(a):
    # Enter your code here
    if len(a) <= 1:
        return a
    pivot = a[0]
    small = [x for x in a if x < pivot]
    equal = [x for x in a if x == pivot]
    large = [x for x in a if x > pivot]

    return quicksort(large) + equal + quicksort(small)

if __name__ == "__main__":
    # you can test your function by using the following
    print(quicksort([1, 2, 4, 5, 1, 3, 2, -1]))
