import numpy as np
from p2 import reshape_and_translate  # Make sure p2.py is in the same directory

def test_reshape_and_translate():
    # Test Case 1: Sample Run
    array = np.arange(1, 17)
    new_shape = (2, 8)
    shift_r = 1
    shift_c = 2
    expected_output = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 2, 3, 4, 5, 6]
    ])
    result = reshape_and_translate(array, new_shape, shift_r, shift_c)
    if np.array_equal(result, expected_output):
        print("Test Case 1 Passed (Sample Run)")
        print("Result:")
        print(result)
    else:
        print("Test Case 1 Failed")
        print("Expected:")
        print(expected_output)
        print("Got:")
        print(result)

    # Test Case 2: No Shift
    array = np.arange(1, 10)
    new_shape = (3, 3)
    shift_r = 0
    shift_c = 0
    expected_output = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    result = reshape_and_translate(array, new_shape, shift_r, shift_c)
    if np.array_equal(result, expected_output):
        print("Test Case 2 Passed (No Shift)")
    else:
        print("Test Case 2 Failed")

    # Test Case 3: Shift Beyond Bounds
    array = np.arange(1, 13)
    new_shape = (3, 4)
    shift_r = 4  # Shift more than number of rows
    shift_c = 5  # Shift more than number of columns
    expected_output = np.zeros((3, 4))
    result = reshape_and_translate(array, new_shape, shift_r, shift_c)
    if np.array_equal(result, expected_output):
        print("Test Case 3 Passed (Shift Beyond Bounds)")
    else:
        print("Test Case 3 Failed")

    # Test Case 4: Negative Shift
    array = np.arange(1, 13)
    new_shape = (3, 4)
    shift_r = -1
    shift_c = -2
    expected_output = np.array([
        [7, 8, 0, 0],
        [11, 12, 0, 0],
        [0, 0, 0, 0]
    ])
    result = reshape_and_translate(array, new_shape, shift_r, shift_c)
    if np.array_equal(result, expected_output):
        print("Test Case 4 Passed (Negative Shift)")
        print("Result:")
        print(result)
    else:
        print("Test Case 4 Failed")
        print("Expected:")
        print(expected_output)
        print("Got:")
        print(result)

    # Test Case 5: Non-Rectangular Shift
    array = np.arange(1, 21)
    new_shape = (4, 5)
    shift_r = 2
    shift_c = 1
    expected_output = np.array([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 2, 3, 4],
        [0, 6, 7, 8, 9]
    ])
    result = reshape_and_translate(array, new_shape, shift_r, shift_c)
    if np.array_equal(result, expected_output):
        print("Test Case 5 Passed (Non-Rectangular Shift)")
    else:
        print("Test Case 5 Failed")

if __name__ == "__main__":
    test_reshape_and_translate()
