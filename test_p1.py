import os
import sys
# Ensure the working directory is the same as the directory where the file is located.
current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)

# Exercise 1
if (os.path.isfile('p1.py')):
    try:
        from p1 import divisible_sublist
        print('Load p1.py')
        test1 = [[21, 25, 9, 16, 28], [12, 43, 4, 66, 123, 654]]
        test2 = [3, 4]
        test3 = [7, 9]
        expected = [([21, 9, 28], [21], [25, 16]), ([12, 4], [], [43, 66, 123, 654])]
        try:
            print('Testing...')
            answer = list(map(divisible_sublist, test1, test2, test3))
            if answer == expected:
                print("You passed all the tests!")
            else:
                print("Wrong answer, you failed the tests!")
        except:
            print('Runtime error when testing divisible_sublist, please check your code!')
    except:
        print('Cannot load divisible_sublist, please check the function name or syntax.')
else:
    print('Cannot find p1.py, please put p1.py and this test script in the same folder.')
