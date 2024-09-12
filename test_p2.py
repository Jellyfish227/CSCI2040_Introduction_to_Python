import os
if os.name == 'posix':
    import pexpect as exp
else:
    import wexpect as exp


# Global settings
script_name = "p2.py"
debug_mode = True
delay_before_send = 0.1


# Test case data
class TestCase:
    pass


class TestCase1(TestCase):
    case_id = 1
    inputs = ['2']
    outputs = [
        'Enter h: 2\r\n' +
        ' /\\\r\n' +
        '/__\\'
    ]


class TestCase2(TestCase):
    case_id = 2
    inputs = ['5']
    outputs = [
        'Enter h: 5\r\n' +
        '    /\\\r\n' +
        '   /  \\\r\n' +
        '  /    \\\r\n' +
        ' /      \\\r\n' +
        '/________\\'
    ]


class TestCase3(TestCase):
    case_id = 3
    inputs = ['0', '-1', '1', '31', '7']
    outputs = [
        'Enter h: 0\r\n' +
        'Invalid input for h!\r\n' +
        'Enter h: -1\r\n' +
        'Invalid input for h!\r\n' +
        'Enter h: 1\r\n' +
        'Invalid input for h!\r\n' +
        'Enter h: 31\r\n' +
        'Invalid input for h!\r\n' +
        'Enter h: 7\r\n' +
        '      /\\\r\n' +
        '     /  \\\r\n' +
        '    /    \\\r\n' +
        '   /      \\\r\n' +
        '  /        \\\r\n' +
        ' /          \\\r\n' +
        '/____________\\'
    ]


# Run test cases
def run_test_case(tc: TestCase):

    def decode(output: bytes | str):
        return output.decode() if isinstance(output, bytes) else output

    def out_eq(output: bytes | str, expected: str):
        return decode(output) == expected

    def print_debug_info(*args):
        print("Produced:", args[0], sep='\n')
        print("Expected:", args[1], sep='\n')

    print(f"Running Test Case {tc.case_id} ...")

    # Spawn a child process to run the script to be tested
    child = exp.spawn('python ' + script_name)
    child.delaybeforesend = delay_before_send

    passed = True
    for user_in in tc.inputs:   # send (multiple) user inputs
        child.sendline(user_in)

    # Wait for the script's response
    child.expect(exp.EOF)

    # Get the script's output
    pgm_out = child.before.rstrip()  # strip the EOL char

    exp_out = tc.outputs[0]  # (single) expected output
    if not out_eq(pgm_out, exp_out):
        if debug_mode:
            print_debug_info(decode(pgm_out), exp_out)
        passed = False

    # Close the child process
    child.close()

    return passed


if __name__ == '__main__':

    if not os.path.isfile(script_name):
        print(f'{script_name} does not exist!', 'Check your script name.')
        print('Make sure it is put in the same folder with this test script.')
        raise SystemExit(1)

    test_cases = [TestCase1(), TestCase2(), TestCase3()]

    passed_cases = 0
    for test_case in test_cases:
        if run_test_case(test_case):
            print(f'Test case {test_case.case_id}: Passed!\n')
            passed_cases += 1
        else:
            print(f'Test case {test_case.case_id}: Failed!\n')

    if passed_cases == len(test_cases):
        print("Congrats! You passed all test cases!")
