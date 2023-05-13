def findDigits(n):
    str_n=str(n)
    count=0
    for c in str_n:
        if int(c)!=0 and n%int(c)==0:
            count+=1
    return count

n= int(input())
findDigits(n)
