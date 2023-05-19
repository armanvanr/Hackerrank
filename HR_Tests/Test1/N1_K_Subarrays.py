arr1 = [5, 10, 11, 9, 5]
k1 = 5


def ksub1(k, nums):  # 5/12 passed
    count = 0
    for i in range(len(nums)):
        arr = []
        for j in range(i, len(nums)):
            arr.append(nums[j])
            if sum(arr) % k == 0:
                count += 1
    return count


def ksub2(k, nums):  # 6/12 passed
    count = 0
    for i in range(len(nums)):
        sums = 0
        for j in range(i, len(nums)):
            sums += nums[j]
            if sums % k == 0:
                count += 1
    return count


def ksub3(k, nums):  # ?/12 passed
    n = len(nums)
    count = 0
    mods = [num % k for num in nums]
    for i in range(n):
        sums = 0
        for j in range(i, n):
            sums += mods[j]
            if sums % k == 0:
                count += 1
    return count


# print(ksub3(5,[5973,101021,11271,9139819,5180310,1261930,362,4215,1290140]))

if __name__ == "__main__":
    # print(ksub1(k1, arr1))
    # print(ksub1(3,[1,2,3,4,1]))
    # print(ksub1(4,[2,3,5,6,7,4,3]))

    # print(ksub2(k1, arr1))
    print(ksub3(k1, arr1))
