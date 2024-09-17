import os
if os.name == 'posix':
    import pexpect as exp
else:
    import wexpect as exp


# Global settings
script_name = "p4.py"
debug_mode = True
delay_before_send = 0.1


# Test case data
class TestCase:
    pass


class TestCase1(TestCase):
    case_id = 1
    inputs = ['10000', '5', '4', '5']
    outputs = [
'Enter the initial principal amount ($P): 10000',
'Enter the annual interest rate (r%): 5',
'Enter the number of compounding periods per year (n = 1, 2, 4, 12): 4',
'Enter the number of years (t): 5',
'Year |     Amount    | Interest Earned',
'----------------------------------------',
'   1 | $    10509.45 | $        509.45',
'   2 | $    11044.86 | $        535.41',
'   3 | $    11607.55 | $        562.68',
'   4 | $    12198.90 | $        591.35',
'   5 | $    12820.37 | $        621.48',
'Summary:',
'Total interest earned: $2820.37',
'Final account balance: $12820.37'
    ]


class TestCase2(TestCase):
    case_id = 2
    inputs = ['5500', '3', '12', '7']
    outputs = [
'Enter the initial principal amount ($P): 5500',
'Enter the annual interest rate (r%): 3',
'Enter the number of compounding periods per year (n = 1, 2, 4, 12): 12',
'Enter the number of years (t): 7',
'Year |     Amount    | Interest Earned',
'----------------------------------------',
'   1 | $     5667.29 | $        167.29',
'   2 | $     5839.66 | $        172.38',
'   3 | $     6017.28 | $        177.62',
'   4 | $     6200.30 | $        183.02',
'   5 | $     6388.89 | $        188.59',
'   6 | $     6583.22 | $        194.32',
'   7 | $     6783.45 | $        200.23',
'Summary:',
'Total interest earned: $1283.45',
'Final account balance: $6783.45'
    ]


class TestCase3(TestCase):
    case_id = 3
    inputs = ['100', '2.3', '12', '4']
    outputs = [
'Enter the initial principal amount ($P): 100',
'Enter the annual interest rate (r%): 2.3',
'Enter the number of compounding periods per year (n = 1, 2, 4, 12): 12',
'Enter the number of years (t): 4',
'Year |     Amount    | Interest Earned',
'----------------------------------------',
'   1 | $      102.32 | $          2.32',
'   2 | $      104.70 | $          2.38',
'   3 | $      107.14 | $          2.43',
'   4 | $      109.63 | $          2.49',
'Summary:',
'Total interest earned: $9.63',
'Final account balance: $109.63'
    ]


# Run test cases
def run_test_case(tc: TestCase, timeout = 60):

    def decode(output: bytes | str):
        return output.decode() if isinstance(output, bytes) else output

    def out_eq(output: bytes | str, expected: str):
        return decode(output) == expected

    def print_debug_info(*args):
        print("Produced:", args[0])
        print("Expected:", args[1])
        print(f'Output line {args[2]} may be incorrect!')

    print(f"Running Test Case {tc.case_id} ...")

    # Spawn a child process to run the script to be tested
    child = exp.spawn('python ' + script_name, timeout = timeout)
    child.delaybeforesend = delay_before_send

    passed = True
    line_num = 1
    for user_in, exp_out in zip(tc.inputs, tc.outputs):
        # Send the user input and read the program output
        child.sendline(user_in)
        pgm_out = child.readline().rstrip()
        if not out_eq(pgm_out, exp_out):
            if debug_mode:
                print_debug_info(decode(pgm_out), exp_out, line_num)
            passed = False
        line_num += 1

    # Read the rest of output lines produced by the program
    if len(tc.outputs) > len(tc.inputs):
        for i in range(len(tc.inputs), len(tc.outputs)):
            pgm_out = child.readline().rstrip()
            if not out_eq(pgm_out, tc.outputs[i]):
                if debug_mode:
                    print_debug_info(decode(pgm_out), tc.outputs[i], line_num)
                passed = False
            line_num += 1

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
