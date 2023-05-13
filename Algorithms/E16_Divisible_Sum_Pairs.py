def divisibleSumPairs(n, k, ar):
    count = 0
    i = 0
    while i < n - 1:
        j = i + 1
        while j < n:
            if (ar[i] + ar[j]) % k == 0:
                count += 1
            j += 1
        i += 1
    return count


print(divisibleSumPairs(6, 5, [1, 2, 3, 4, 5, 6]))
# print(divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]))


def div_sum_pairs(n, k, ar):
    count = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                count += 1
    return count

print(div_sum_pairs(6, 5, [1, 2, 3, 4, 5, 6]))
