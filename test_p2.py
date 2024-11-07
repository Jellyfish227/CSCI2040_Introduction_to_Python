import os
current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)

if os.path.isfile("p2.py"):
    try:
        import p2

        print("Successfully load p2.py")
        expected1 = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
        expected2 = [1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]
        expected3 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        expected4 = [1, 4, 9, 16]
        expected5 = [0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]
        expected6 = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800]
        expected7 = ["ALICE", "BOB", "DIANA", "ETHAN", "HANNAH"]
        expected8 = {
            1:"1*1=1",
            2:"1*2=2 2*2=4",
            3:"1*3=3 2*3=6 3*3=9",
            4:"1*4=4 2*4=8 3*4=12 4*4=16",
            5:"1*5=5 2*5=10 3*5=15 4*5=20 5*5=25",
            6:"1*6=6 2*6=12 3*6=18 4*6=24 5*6=30 6*6=36",
            7:"1*7=7 2*7=14 3*7=21 4*7=28 5*7=35 6*7=42 7*7=49",
            8:"1*8=8 2*8=16 3*8=24 4*8=32 5*8=40 6*8=48 7*8=56 8*8=64",
            9:"1*9=9 2*9=18 3*9=27 4*9=36 5*9=45 6*9=54 7*9=63 8*9=72 9*9=81",
        }
        try:
            print("Testing...")
            if (expected1 == p2.list1):
                print("You passed the test for list1!")
            else:
                print('Wrong answer, you failed the test for list1!')
                print("Expected answer: ", expected1)
                print("Your answer is: ", p2.list1)
            if (expected2 == p2.list2):
                print("You passed the test for list2!")
            else:
                print('Wrong answer, you failed the test for list2!')
                print("Expected answer: ", expected2)
                print("Your answer is: ", p2.list2)
            if (expected3 == p2.list3):
                print("You passed the test for list3!")
            else:
                print('Wrong answer, you failed the test for list3!')
                print("Expected answer: ", expected3)
                print("Your answer is: ", p2.list3)
            if (expected4 == p2.list4):
                print("You passed the test for list4!")
            else:
                print('Wrong answer, you failed the test for list4!')
                print("Expected answer: ", expected4)
                print("Your answer is: ", p2.list4)
            if (expected5 == p2.list5):
                print("You passed the test for list5!")
            else:
                print('Wrong answer, you failed the test for list5!')
                print("Expected answer: ", expected5)
                print("Your answer is: ", p2.list5)
            if (expected6 == p2.list6):
                print("You passed the test for list6!")
            else:
                print('Wrong answer, you failed the test for list6!')
                print("Expected answer: ", expected6)
                print("Your answer is: ", p2.list6)
            if (expected7 == p2.list7):
                print("You passed the test for list7!")
            else:
                print('Wrong answer, you failed the test for list7!')
                print("Expected answer: ", expected7)
                print("Your answer is: ", p2.list7)
            if (expected8 == p2.dict1):
                print("You passed the test for dict1!")
            else:
                print('Wrong answer, you failed the test for dict1!')
                print("Expected answer: ", expected8)
                print("Your answer is: ", p2.dict1)
        except Exception as e:
            print("Error:",e)
            print("Runtime error when testing p2, please check your code")
    except Exception as e:
        print("Error:",e)
        print("Cannot load p2, please check the file")
else:
    print(
        "Cannot find p2.py, please put p2.py and this test script in the same folder."
    )
