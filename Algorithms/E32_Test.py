from E32_Save_The_Prisoners import saveThePrisoner


t = int(input().strip())

for t_itr in range(t):
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    s = int(first_multiple_input[2])

    result = saveThePrisoner(n, m, s)

    print(str(result) + '\n')
