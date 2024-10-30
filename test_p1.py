import os
current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)

if os.path.isfile('p1.py'):
    try:
        from p1 import non_unique
        print('Successfully load p1.py')
        test_case = [['a', 'b', 'c', 'a', 'b', 'd'], [], ['abc', 'def', 'abc', 'xyz', 'def']]
        expected = [['a', 'b'], [], ['abc', 'def']]
        try:
            print('Testing...')
            answer = list(map(non_unique, test_case))
            if answer == expected:
                print('You passed all the tests!')
            else:
                print('Wrong answer, you failed some of the tests!')
        except:
            print('Runtime error when testing unique, please check your code')
    except:
        print('Cannot load non_unique function, please check the function name or syntax')
else:
    print("Cannot find p1.py, please put p1.py and this test script in the same folder.")
