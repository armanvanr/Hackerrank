def bonAppetit(bill, k, b):
    bill.pop(k)
    b_actual = (sum(bill)) // 2
    diff = b - b_actual
    if diff == 0:
        print("Bon Appetit")
    else:
        print(diff)


b1 = [3, 10, 2, 9]
print(bonAppetit(b1, 1, 12))
