import numpy as np

def transpose(A):
    row, col = A.shape
    tempMat = np.zeros((col, row))

    for i in range(row):
        for j in range(col):
            tempMat[j][i] = A[i][j]
    return tempMat

def matrix_calculation(A, B):
    if A.shape[0] != B.shape[1] or A.shape[1] != B.shape[0]:
        print("Please check the shape of matrix A and B")
        return None
    C = transpose(A)
    C += B
    return C

if __name__ == '__main__':
    A = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8]])
    B = np.array([[9, 10],
                  [11, 12],
                  [13, 14],
                  [15, 16]])
    print(transpose(A))