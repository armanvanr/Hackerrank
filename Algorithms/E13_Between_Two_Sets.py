def getTotalX(a, b):
    count=0
    
    for num in range(max(a),min(b)+1):
        if all([num%e==0 for e in a]):
            if all([e%num==0 for e in b]):
                count+=1
    return count
# print(getTotalX([2,4],[24,32,96]))

def get_total_x(a,b):
    count=0
    for num in range(max(a),min(b)+1):
        y,z = [],[]
        for e in a:
            y.append(num%e==0)
        if all(y):
            for f in b:
                z.append(f%num == 0)
            if all(z):
                count+=1
    return count
print(get_total_x([2,4],[24,32,96]))

def gtx(a,b):
    count=0
    for num in range(max(a),min(b)+1):
        y,z = [],[] # bisa pakai count lalu bandingkan y dan z dengan len a & len b
        for e in a:
            if num%e==0: y.append(num)
        if len(y)==len(a):
            for f in b:
                if f%num==0: z.append(num)
            if len(z)==len(b):
                count+=1
    return count