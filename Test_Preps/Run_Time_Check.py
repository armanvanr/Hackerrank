import time
import sys

sys.path.append('A:\\Makers Institute\\Codes\\Week 2\\Hackerrank\\HR_Tests\\Test1')

from N1_K_Subarrays import ksub1, ksub2, ksub3

arr1 = [5, 10, 11, 9, 5]
k1 = 2

# CODE 1
start1 = time.time()
print(ksub1(k1, arr1))
end1 = time.time()

# CODE 2
start2 = time.time()
print(ksub2(k1, arr1))
end2 = time.time()

# CODE 3
start3 = time.time()
print(ksub3(k1, arr1))
end3 = time.time()

# print the difference between start
# and end time in milli. secs
# print("The time of execution of above program is :",
#       (end1-start1) * 10**3, "ms")
dur1=(end1-start1)*(10**3)
dur2=(end2-start2)*(10**3)
dur3=(end3-start3)*(10**3)
print("durasi 1,2,3:", dur1, dur2, dur3)
