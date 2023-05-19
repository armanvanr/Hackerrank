def gainMaxValue(security_val, k): #9/15 allowed time 10s
    n = len(security_val)
    max_val = -1000
    for i in range(n):
        val_sum = 0
        for j in range(i,n,k):
            val_sum += security_val[j]
        if val_sum > max_val: max_val = val_sum
    return max_val


if __name__ == "__main__":
    # print(gainMaxValue([3, 5, -2, -4, 9, 16], 2))
    print(gainMaxValue([2, 5, -8, -6, -7], 3)) #-2