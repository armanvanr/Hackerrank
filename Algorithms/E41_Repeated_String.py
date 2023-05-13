def repeatedString(s, n):
    x = len(s)
    r = n//x
    p = n%x
    res = s.count("a")*r + s[:p].count("a")
    return res

# x: length of string
# r: number of repeating string
# p: modulo result as last index