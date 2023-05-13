def pickingNumbers(a):    
    unique = sorted(list(set(a)))
    freq = []
    for num in unique:
        freq.append(a.count(num))
    longest = max(freq)
    if len(unique)>1:
        for index in range(len(unique) - 1):
            if unique[index+1] - unique[index] == 1 and freq[index] + freq[index + 1] > longest:
                longest = freq[index] + freq[index + 1]
    else:
        longest = freq[0]
    return longest

pickingNumbers([4,4,5,5,6,6,8,8,8,13,13,13,13,13,13,13,13])
4,5,6,8
2,2,2,3
[99,99,99,99]