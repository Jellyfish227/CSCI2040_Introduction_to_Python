import os
# Ensure the working directory is the same as the directory where the file is located.
current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)

# Exercise 3
if (os.path.isfile('p3.py')):
    try:
        from p3 import recursive_sqrt
        print('Load p3.py')
        test1 = [2, 29, 47, 52, 10, 778, 999, 666, 45, 9, 15]
        test2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        expected = ['1.41', '5.39', '6.86', '7.21', '3.16', '27.89', '31.61', '25.81', '6.71', '3.00', '3.87']
        try:
            print('Testing...')
            answer = list(map(recursive_sqrt, test1, test2))
            answer = ['%.2f' % elem for elem in answer]
            if answer == expected:
                print("You passed all the tests!")
            else:
                print("Wrong answer, you failed the tests!")
                print("Expected:", expected)
                print("Your answer:", answer)
        except:
            print('Runtime error when testing recursive_pow, please check your code!')
    except:
        print('Cannot load recursive_pow, please check the function name or syntax.')
else:
    print('Cannot find p3.py, please put p3.py and this test script in the same folder.')
