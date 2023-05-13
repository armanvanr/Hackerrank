def getUniqueCharacter(s): # 15/15 passed
    f=[]
    for c in s:
        if s.count(c) == 1:
            f.append(s.index(c) +1)
    if len(f) ==0:
        return -1
    else:
        return min(f)

getUniqueCharacter("sctatisatics")