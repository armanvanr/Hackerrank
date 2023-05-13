def diagonalDifference(arr):
    dia1, dia2 = 0, 0
    n = len(arr)
    i = 0
    while i < n:
        j = 0
        while j < n:
            if i == j:
                dia1 += arr[i][j] # arr[i][i]
            if i + j == n - 1:
                dia2 += arr[i][j] # arr[i][n-i-1]
            j += 1
        i += 1
    res = abs(dia1 - dia2)
    return res

def diagonal_difference(arr):
    n = len(arr)
    dia1 = sum([arr[i][i] for i in range(n)])
    dia2 = sum([arr[i][n-i-1] for i in range(n)])
    return abs(dia1-dia2)

d = [[111, 2, 4],
     [4, 15, 6],
     [10, 8, -12]]
print(diagonalDifference(d))
print(diagonal_difference(d))

# a = [[1, 2],
#      [3, 4]]

# b = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]

# c = [[1, 2, 3, 10],
#      [4, 5, 6, 11],
#      [7, 8, 9, 12],
#      [7, 8, 9, 13]]

