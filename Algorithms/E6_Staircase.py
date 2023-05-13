num = int(input("Input height: "))
def staircase(n):
    i=0
    while i<n:
        print(' '*(n-i-1)+'#'*(i+1))
        i+=1
staircase(num)

def stair_case(n):
    for i in range(n):
        print(' '*(n-i-1)+'#'*(2*i+1))
stair_case(num)