def kaprekarNumbers(p, q):
    res = []
    for num in range(p, q + 1):
        # banyak digit dari num, misal 9 -> d=1
        d = len(str(num))

        # kuadrat (square)
        square = num**2
        str_sq = str(square)

        # panjang kuadrat, misal 9^2=81 -> m=2
        m = len(str_sq)

        # slice left
        l = str_sq[:m-d]
        if l == '':
            l = '0'

        # slice right
        r = str_sq[m-d:]

        if int(l)+int(r) == num:
            res.append(num)
    if len(res) == 0:
        print("INVALID RANGE")
    else:
        print(*res)


kaprekarNumbers(1, 100000)
