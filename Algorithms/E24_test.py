from E24_Cats_And_A_Mouse import catAndMouse

q = int(input())

for q_itr in range(q):
    xyz = input().split()

    x = int(xyz[0])

    y = int(xyz[1])

    z = int(xyz[2])

    print("x,y,z: ", x, y, z)
    print(xyz)
    print(type(xyz))
    result = catAndMouse(x, y, z)


