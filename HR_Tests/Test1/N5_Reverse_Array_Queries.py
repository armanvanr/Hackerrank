def performOperations(arr, operations): # 15/15 passed
    for op in operations:
        left = arr[: op[0]]
        right = arr[op[1]+1 :]
        to_reverse = arr[op[0]:op[1]+1]
        to_reverse.reverse()
        arr = left + to_reverse + right
        print("left:", left)
        print("right:", right)
        print("reverse:", to_reverse)

oper = [[0, 9], [4, 5], [3, 6], [2, 7], [1, 8], [0, 9]]
(performOperations([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], oper))
