import numpy as np

def reshape_and_translate( array , new_shape , shift_r , shift_c ):
    
    array = np.reshape(array, new_shape)
    
    tmpArr = np.copy(array)
    if shift_r > 0:
        for i in range(shift_r):
            tmpArr[i] = array[i+1]
    if shift_c > 0:
        for i in range(shift_c):
            tmpArr = np.roll(tmpArr, 1, axis=1)
    # array = np.roll(array, shift_r, axis=0)
    # array = np.roll(array, shift_c, axis=1)

    # handle out of bound situations
    
    return array

if __name__ == '__main__':
