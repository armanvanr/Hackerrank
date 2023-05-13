def miniMaxSum(arr):
    arr = sorted(arr)
    min_sum= sum(arr[0:4])
    max_sum = sum(arr[1:5])
    print(min_sum, max_sum)

a = [1,2,3,4,5]
b = [1,3,5,7,9]
miniMaxSum(b)
miniMaxSum(a)

def mini_max_sum(arr):
    min_sum = sum(arr)-max(arr)
    max_sum = sum(arr)-min(arr)
    print(min_sum, max_sum)