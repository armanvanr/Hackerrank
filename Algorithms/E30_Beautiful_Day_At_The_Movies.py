def beautifulDays(i, j, k):
    count = 0
    for num in range(i,j+1):
        rev_num=int(str(num)[::-1])
        if abs(num-rev_num) % k == 0:
            count+=1
    return count

def beautiful_days(i,j,k):
    f = [1 for num in range(i,j+1) if (abs(num-(int(str(num)[::-1])))) % k == 0]
    return sum(f)