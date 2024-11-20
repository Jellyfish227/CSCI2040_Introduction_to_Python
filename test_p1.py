import numpy as np
from p1 import matrix_calculation  # Make sure p1.py is in the same directory


def test_matrix_calculation():
    # Test Case 1: Compatible matrices (Sample Run)
    A = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8]])
    B = np.array([[9, 10],
                  [11, 12],
                  [13, 14],
                  [15, 16]])
    expected_C = A.T + B
    result_C = matrix_calculation(A, B)

    if result_C is not None and np.array_equal(result_C, expected_C):
        print("Test Case 1 Passed")
        print("Matrix C:")
        print(result_C)
    else:
        print("Test Case 1 Failed")

    # Test Case 2: Incompatible shapes
    A = np.array([[1, 2, 3],
                  [4, 5, 6]])  # Shape: (2, 3)
    B = np.array([[7, 8],
                  [9, 10]])  # Shape: (2, 2)
    result_C = matrix_calculation(A, B)

    if result_C is None:
        print("Test Case 2 Passed (Incompatible shapes detected)")
    else:
        print("Test Case 2 Failed")

    # Test Case 3: Different compatible matrices
    A = np.array([[2, 4],
                  [6, 8],
                  [10, 12]])
    B = np.array([[1, 3, 5],
                  [7, 9, 11]])
    expected_C = A.T + B
    result_C = matrix_calculation(A, B)

    if result_C is not None and np.array_equal(result_C, expected_C):
        print("Test Case 3 Passed")
        print("Matrix C:")
        print(result_C)
    else:
        print("Test Case 3 Failed")

    # Test Case 4: Edge case with zero matrices
    A = np.zeros((2, 3))
    B = np.zeros((3, 2))
    expected_C = A.T + B
    result_C = matrix_calculation(A, B)

    if result_C is not None and np.array_equal(result_C, expected_C):
        print("Test Case 4 Passed")
        print("Matrix C:")
        print(result_C)
    else:
        print("Test Case 4 Failed")


if __name__ == "__main__":
    test_matrix_calculation()
