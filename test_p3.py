import subprocess
import os
current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)

def check_ans(case_no, code_ans, expect_ans,):
    global FLAGS_final_score
    if code_ans == expect_ans:
        print('You passed the test case ' + str(case_no) + ' :)')
    else:
        print('You failed in the test case ' + str(case_no) + ' :(')
        print('The expected answer is: ' + expect_ans)
        print('But your answer is: ' + code_ans)


FLAGS_final_score = 0
cmd = 'python called_by_test_p3.py'
code_ans_list = subprocess.check_output(cmd, shell=True)
code_ans_list = code_ans_list.splitlines()

expect_ans_list = ['list length 0',
                   'Current linked list: 20-->15-->10-->20-->none',
                   'True',
                   'False',
                   'list length 5',
                   'Current linked list: 30-->20-->15-->10-->20-->none',
                   'Current linked list: 30-->15-->10-->20-->none']


for i in range(7):
    case_no = i + 1
    code_ans = code_ans_list[i].decode()
    expect_ans = expect_ans_list[i]
    check_ans(case_no, code_ans, expect_ans)

print('More details about those test cases can be found in called_by_test_p3.py')
