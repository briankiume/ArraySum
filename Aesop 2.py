import numpy as np


def sum_arr(arr):
    arr = np.array(arr)
    tot = np.sum(arr)

    return tot


print(sum_arr([1, 2, 4, 6363, 732]))


# ----------------->

def sum_arr2(arr):
    tot = 0
    for x in arr:
        tot += x

    return tot


print(sum_arr2([1, 2, 4, 6363, 732]))
