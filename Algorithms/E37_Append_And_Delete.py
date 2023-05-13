def append_and_delete(s,t,k):
    if k >= len(s) + len(t):return "Yes"
    index = getIndex(s,t) if len(s)>len(t) else getIndex(t,s)
    k -= len(s)-index
    k -= len(t)-index
    
    return "Yes" if k%2 == 0 and k >= 0 else "No"
    
        
def getIndex(big,small):
    index = 0   
    while index < len(small):
        if small[index] != big[index]:
            break
        index += 1
    return index


def appendAndDelete(s, t, k):
    i=0
    ns=len(s)
    nt=len(t)
    while i<min(ns,nt) and s[i] == t[i]:
        # print(s[i], t[i])
        i+=1
    
    # if (ns-i + nt-i) <= k:
        # return "Yes"
    if (k-(ns-i + nt-i))%2 == 0:
        return "YES"
    else:
        return "No"
    
    
    
print("ashley")
print(appendAndDelete("Ashley", "Ash", 2)) #NO
print()

print("hackerhappy")
print(appendAndDelete("hackerhappy", "hackerrank", 9)) #YES
print()

print("zzzzz")
print(appendAndDelete("zzzzz", "zzzzzzz", 4)) #YES
print()

x="asdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv"
y="bsdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv"

print("asd vs asd")
print(appendAndDelete(x, x, 20)) #YES
print()

print("asd vs bsd")
print(appendAndDelete(x, y, 100)) #NO
print()

print("y vs yu")
print(appendAndDelete("y", "yu", 2)) #NO
# print(append_and_delete("y", "yu", 2)) #NO
print()

print("abcdz vs abcdert")
print(appendAndDelete("abcd", "abcdert", 10)) #NO
print(append_and_delete("abcd", "abcdert", 10)) #NO

