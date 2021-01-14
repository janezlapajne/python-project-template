import numpy as np


def check_arr(arrA, arrB):
    return np.all(np.squeeze(np.isclose(arrA, arrB)))


