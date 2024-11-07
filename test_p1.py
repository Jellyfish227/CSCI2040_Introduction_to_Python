import os
import subprocess
current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)


if os.path.isfile('p1.py'):
    try:
        from p1 import RPNCalculator
        print('Successfully load p1.py')
        calc = RPNCalculator()
        try:
            print('Testing...')
            answer1 = calc.eval("4 3 - 2 * 3 %")
            expected1 = 2
            if answer1 == expected1:
                print('You passed the test!')
            else:
                print('Wrong answer, you failed the test!')
                print("Expected answer: ", expected1)
                print("Your answer is: ", answer1)
        except Exception as e:
            print("Error:",e)
            print('Runtime error when testing RPNCalculator, please check your code')
    except Exception as e:
        print("Error:",e)
        print('Cannot load RPNCalculator, please check the function name or syntax')
else:
    print("Error: Cannot find p1.py, please put p1.py and this test script in the same folder.")
