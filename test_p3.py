import os
import sys
if (os.name == 'posix'):
    import pexpect as exp
else:
    import wexpect as exp

def test_script(input_string, choice, expected_output):
    try:
        child = exp.spawn('python p3.py')
        # # Enable logging for debugging
        # child.logfile = sys.stdout.buffer

        child.expect('Enter a string: ')
        child.sendline(input_string)
        child.expect('Choose a transformation:')
        child.expect('1. Convert to uppercase')
        child.expect('2. Replace vowels with \'*\'')
        child.expect('3. Reverse the string')
        child.expect('4. Append \'EVEN\' or \'ODD\'')
        child.expect('Enter your choice: ')
        child.sendline(str(choice))
        if 1 <= int(choice) <= 4:
            child.expect('Transformed string: ')
            child.expect(expected_output)
            child.expect('Transformation complete. Goodbye!')
        else:
            child.expect('Invalid choice. No transformation applied.')
            child.expect('Transformed string: ')
            child.expect(expected_output)
            child.expect('Transformation complete. Goodbye!')
        print(f"Test for input '{input_string}' passed!")
        return True
    except Exception as e:
        print(e)
        print(f"Test for input '{input_string}' failed! ")
        return False

# Sample Test Cases
successful_cases = 0
test_cases = [
    ("Python", 4 , 'PythonEVEN'),
    ("HongKong", 1 , 'HONGKONG'),
    ("I love Python!", 2 , '\* l\*v\* Pyth\*n!'),
    ("programming", 3 , 'gnimmargorp'),
    ("CSCI2040", 5 , 'CSCI2040')
]

for input_string, choice, expected_output in test_cases:
    if test_script(input_string, choice, expected_output):
        successful_cases += 1

print(f"\n{successful_cases} out of {len(test_cases)} test cases passed.")
