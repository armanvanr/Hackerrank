# def jumpingOnClouds(c, k):
#     e=100
#     n=len(c)
#     c.append(c[0])
#     i=k
#     for i in range(k,n+1,k):
#         if c[i] == 1:
#             e -=2
#         e-=1
#     return e
# print(jumpingOnClouds([0,0,1,0],2))
# print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 1, 0],2))
# print(jumpingOnClouds([1, 1, 1, 0, 1, 1, 0, 0, 0, 0],3))

# def jumping_on_clouds(c,k):
#     e=100
#     n=len(c)
#     c.append(c[0])
#     i=k
#     while k<= i <n+1:
#         if c[i] == 1:
#             e -=2
#         e-=1
#         i+=k
#     return e
# print(jumping_on_clouds([0,0,1,0],2))
# print(jumping_on_clouds([0, 0, 1, 0, 0, 1, 1, 0],2))
# print(jumping_on_clouds([1, 1, 1, 0, 1, 1, 0, 0, 0, 0],3))

def joc(c,k):
    # inisialisasi energi awal e, banyak awan n, indeks list i, dan variabel digit terakhir x
    e=100
    n=len(c)
    print("i","x","c",)
    i,x=0,-1

    # selama i kurang dari banyak awan dan x tidak sama dengan nol
    while i < n*n and x !=0:
        
        x=(i+k)%n
        print(i, x, c[x])
        if c[x] == 1:
            e -=2
        e-=1
        i+=k
    return e

# print(joc([10,20,30,40,50,60,70,80,90],2))
print(joc([1, 1, 1, 0, 1, 1, 0, 0, 0, 0],3))
print(joc([0, 0, 1, 0, 0, 1, 1, 0],2))