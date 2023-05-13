def rotateLeft(d, arr):
    for _ in range(d):
        arr.append(arr[0])
        arr.pop(0)
    return arr
