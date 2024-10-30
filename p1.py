def non_unique(input_list):
    ## Enter your code here
    result = []
    temp = {}
    for i in input_list:
        if i not in temp:
            temp[i] = 1
        else:
            temp[i] += 1
    for i in temp:
        if temp[i] > 1:
            result.append(i)
    return result

if __name__ == '__main__':
    # you can test your function by using the following
    input_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'grape']
    print(input_list)
    output_list = non_unique(input_list)
    print(output_list)

