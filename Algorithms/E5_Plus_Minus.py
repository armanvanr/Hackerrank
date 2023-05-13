def plusMinus(arr):
    plus, minus = 0,0
    n = len(arr)
    for num in arr:
        if num > 0:
            plus += 1
        elif num < 0:
            minus += 1
    zero = (n - plus - minus) / n
    plus = plus / n
    minus = minus / n
    print(format(plus, '.6f'))
    print(format(minus,'.6f'))
    print(format(zero,'.6f'))
a=[1,1,0,-1,-1]
b=[-4,3,-9,0,4,1]
plusMinus(b)
print()

def plus_minus_dict(arr):
    n = len(arr)
    d = {"plus":0, "minus":0, "zero":0}
    for num in arr:
        if num>0:
            d['plus']+=1
        elif num<0:
            d['minus']+=1
        else:
            d['zero']+=1
    print(format(d["plus"]/n, '.6f'))
    print(format(d["minus"]/n,'.6f'))
    print(format(d["zero"]/n,'.6f'))

plus_minus_dict(b)