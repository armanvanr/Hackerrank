def getUniqueCharacter(s): # 15/15 passed
    f=[]
    for c in s:
        if s.count(c) == 1:
            f.append(s.index(c) +1)
    if len(f) ==0:
        return -1
    else:
        return f[0]
print(getUniqueCharacter("statisatics"))
print(getUniqueCharacter("statistics"))
print(getUniqueCharacter("statitic"))

def guc(s): # 15/15 passed
    for c in s:
        if s.count(c) == 1: return s.index(c) +1
    return -1

# Diberikan sebuah string yang memuat huruf-huruf
# Jika ada karakter unik, return nomor urutan karakter tersebut
# apabila ada lebih dari satu karakter unik, return nomor urut terkecil
# Jika tidak ada karakter unik, return -1