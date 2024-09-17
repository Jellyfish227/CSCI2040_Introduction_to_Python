import os
if (os.name == 'posix'):
    import pexpect as exp
else:
    import wexpect as exp

def test_script(input_string, expected_output, timeout=60):
    try:
        child = exp.spawn('python p1.py', timeout=timeout)
        child.expect('Enter a string: ')
        child.sendline(input_string)
        child.expect(expected_output[0])
        child.expect(expected_output[1])
        print(f"Test for input '{input_string}' passed!")
        return True
    except Exception as e:
        print(e)
        print(f"Test for input '{input_string}' failed! ")
        return False

# Sample Test Cases
successful_cases = 0
test_cases = [
    ("CSCI2040", ['The number of alphabetic letters in "CSCI2040" is "4".', 'The most frequent alphabetic letter in "CSCI2040" is "c".']),
    ("Python.py", ['The number of alphabetic letters in "Python.py" is "8".', 'The most frequent alphabetic letter in "Python.py" is "p".']),
    ("I Love Python More than java", ['The number of alphabetic letters in "I Love Python More than java" is "23".','The most frequent alphabetic letter in "I Love Python More than java" is "a".'])
]

for input_string, expected_output in test_cases:
    if test_script(input_string, expected_output):
        successful_cases += 1

print(f"\n{successful_cases} out of {len(test_cases)} test cases passed.")
