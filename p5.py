# your statement follows
def count_digit(test_string):
    count = 0
    for x in test_string:
        if x.isdigit():
            count += 1
    return count

def check_isogram(test_string):
    test_string = test_string.lower()
    largest = 0
    hashtable = dict.fromkeys(list(map(lambda arg: chr(arg), range(ord('a'), ord('z') + 1))), 0)
    hashtable[' '] = 0
    for x in test_string:
        hashtable[x] += 1
        if largest < hashtable[x]:
            largest = hashtable[x]
            if largest > 1:
                return False
    return True

def join(original_string, inserted_list):
    length = len(inserted_list)
    for x in range(1, length * 2 - 1, 2):
        inserted_list.insert(x, original_string)
    new_string = "".join(inserted_list)
    return new_string

def search(test_string, sub):
    string = "".join(test_string)
    return string.rfind(sub)

if __name__ == '__main__':
    test_str = "Alice was born in 2000 and born in hong kong."
    # print(count_digit(test_str))
    # print(check_isogram(test_str))
    # print(search(test_str, "born"))
    # print(search(test_str, "now"))
    # test2='Abcdefghijka'
    # print(search(test2,'cde'))
    # print(check_isogram(test2))
    # test3='-'
    # print(join(test3,['ab','cd','ef']))