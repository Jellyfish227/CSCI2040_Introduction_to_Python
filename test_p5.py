import os
# Ensure the working directory is the same as the directory where the file is located.
current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)

# Exercise 5
if (os.path.isfile('p5.py')):
    try:
        import p5 as p5
        print('Load p5.py')
        try:
            print('Testing...')
            test_string = 'Alice was born in 2000 and born in hong kong.'
            test2='abcdefghijk'
            test3='-'
            actual_ans = []
            actual_ans.append(p5.count_digit(test_string))
            actual_ans.append(p5.check_isogram(test_string))
            actual_ans.append(p5.search(test_string, 'born'))
            actual_ans.append(p5.search(test_string, 'now'))
            actual_ans.append(p5.search(test2, 'cde'))
            actual_ans.append(p5.check_isogram(test2))
            actual_ans.append(p5.join(test3,['ab','cd','ef']))
            expected_ans = [4, False, 27, -1,2,True,'ab-cd-ef']
            if actual_ans == expected_ans:
                print("You passed all the tests!")
            else:
                print("Wrong answer, you failed the tests!")
        except:
            print('Runtime error when testing TextProcessor, please check your code!')
    except:
        print('Cannot load TextProcessor, please check the class name or syntax.')
else:
    print('Cannot find p5.py, please put p5.py and this test script in the same folder.')
