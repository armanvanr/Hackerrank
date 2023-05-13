def hourglassSum(arr):
    sum_list=[]
    for i in range(0,4):
        # print('i:',i)
        for j in range(0,4):
            top=sum([arr[i][k] for k in range(j,j+3)])
            mid=sum([0, arr[i+1][j+1], 0])
            bottom=sum([arr[i+2][k] for k in range(j,j+3)])
            sum_h=top+mid+bottom
            sum_list.append(sum_h)
            # print('j:',j,'list:',[arr[i][k] for k in range(j,j+3)])
            # print('j:',j,'list:',[0, arr[i+1][j+1], 0])
            # print('j:',j,'list:',[arr[i+2][k] for k in range(j,j+3)])
    print(max(sum_list))
a =[[1, 1, 1, 0, 0, 0,],
    [0, 1, 0, 0, 0, 0,],
    [1, 1, 1, 0, 0, 0,],
    [0, 0, 2, 4, 4, 0,],
    [0, 0, 0, 2, 0, 0,],
    [0, 0, 1, 2, 4, 0,]]
hourglassSum(a)