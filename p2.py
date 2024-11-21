import numpy as np

def reshape_and_translate(array, new_shape, shift_r, shift_c):
    # Reshape the array to the new shape
    reshapedArray = np.reshape(array, new_shape)
    rows, cols = reshapedArray.shape
    
    # Create a temporary array to store the shifted values
    tmpArr = np.zeros_like(reshapedArray)
    
    # Handle the translation with wrapping around
    for i in range(rows):
        for j in range(cols):
            # Calculate new positions with wrapping
            new_row = (i + shift_r)
            new_col = (j + shift_c)
            # Copy the value to the new position
            if not ((new_row < 0) or (new_col < 0) or (new_row >= rows) or (new_col >= cols)):
                tmpArr[new_row, new_col] = reshapedArray[i, j]

    return tmpArr

if __name__ == '__main__':
    reshape_and_translate(np.arange(1,17), (2,8), 1, 2)
    print()
    reshape_and_translate(np.arange(1,13), (3,4), -1, -2)