import re
import math


def encryption(s):
    s = re.sub(" ", "", s)
    col = math.ceil(math.sqrt(len(s)))
    row = math.ceil((len(s)) / 4)
    words = []
    for z in range(row+1):
        words.append(s[z * col : (z + 1) * col])
    print(row, col, len(s), words)
    encr = [""] * col
    for word in words:
        for i in range(len(word)):
            sub = ""
            sub += word[i]
            encr[i] += sub
    res = ' '.join(encr)
    return res

s1= "i know it well"
s2= "chillout"
print(encryption(s2))
