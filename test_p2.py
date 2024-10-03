import os
# Ensure the working directory is the same as the directory where the file is located.
current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)

# Exercise 2
if (os.path.isfile('p2.py')):
    try:
        from p2 import roman_to_decimal
        from p2 import decimal_to_roman
        print('Load p2.py')

        expected1 = [97,29,34]
        answer1=[]
        test_case1 = ['XCVII', 'XXIX', 'XXXIV']

        expected2=['LXXXVIII','LVII','XLVII']
        answer2=[]
        test_case2=[88,57,47]

        len1=len(test_case1)
        len2=len(test_case2)
        try:
            print('Testing...')
            for i in range(len1):
                answer1.append(roman_to_decimal(test_case1[i]))
            for i in range(len2):
                answer2.append(decimal_to_roman(test_case2[i]))

            if answer1 == expected1 and answer2== expected2:
                print("You passed all the tests!")
            elif answer1== expected1 and answer2!=expected2:
                print("You passed the test for the function of roman_to_decimal, but you failed the test for the function of decimal_to_roman!")
            elif answer1!=expected1 and answer2==expected2:
                print("You passed the test for the function of decimal_to_roman, but you failed the test for the function of roman_to_decimal!")
            else:
                print("You failed the test for these two functions.")
        except:
            print('Runtime error when testing roman_to_decimal or decimal_to_roman, please check your code!')
    except:
        print('Cannot load roman_to_decimal or decimal_to_roman, please check the function name or syntax.')
else:
    print('Cannot find p2.py, please put p2.py and this test script in the same folder.')
