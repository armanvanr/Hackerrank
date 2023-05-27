import numpy

def gmm5(arr):  # SOLVED 15/15
    a = numpy.array(arr)
    nums, f = numpy.unique(a, return_counts=True)
    prev = -1
    for i, num in numpy.ndenumerate(nums):
        np = num - prev
        d = f[i] - np
        if d >= 0:
            prev = num
        else:
            prev += f[i] % np
    mex = prev + 1
    return mex