def pageCount(n, p):                            # n=13 maka [0&1 2&3 4&5 6&7 8&9 10&11 12&13] || n=6 maka [0&1 2&3 4&5 6]
    sub = int(n / 2) + 1                        # sub adalah banyaknya pasangan halaman, untuk n=13 sub=7, untuk n=6 sub=4
    if sub % 2 == 0:                            # case 1 jika sub genap contoh [0&1 2&3 4&5 6] punya 1 median
        if n % 2 == 0:                              # case 1a jika n genap, untuk n=6 => n=7
            n = n + 1                               # case 1b jika n ganjil, untuk n=7 => tetap aja n=7
        median = n / 2                              # untuk n=6 atau n=7, median = 3,5 
        if p < median:                              # misal, p=2 atau p=3 => hitung posisi dia dari sampul depan
            position = int(p / 2)
        elif p > median:                            # misal, p=4 atau p=5 => hitung posisi dia dari sampul belakang
            position = int((n - p) / 2)
    else:                                       # case 2 jika sub ganjil contoh [0&1 2&3 4&5 6&7 8&9 10&11 12&13] punya 2 median
        mid_sub = int(sub / 2)                  # hitung median dari pasangan halaman, n=13 maka mid_sub=3
        median1 = mid_sub * 2                   # menentukan 2 nilai tengah, n=13 maka mediannya 6 dan 7
        median2 = median1 + 1
        if n % 2 == 0:                              # case 1a jika n genap, untuk n=6 => n=7
            n = n + 1  
        if p < median1:                             # misal, p=2 atau p=3 => hitung posisi dia dari sampul depan
            position = int(p / 2)
        elif p > median2:                           # misal, p=10 atau p=11 => hitung posisi dia dari sampul belakang
            position = int((n - p) / 2)
        else:                                       # misal, p=6 atau p=7 => posisi dia = mid_sub
            position = mid_sub
    return position                             # mengembalikan posisi terdekat dari kedua sampul

def page_count(n,p):
    if n % 2 == 0:                              # case 1a jika n genap, untuk n=6 => n=7
        n = n + 1 
    return min(p//2, (n-p)//2)

# print(pageCount(5, 3))
# print(pageCount(6,2))
# print(pageCount(5,4))
# print(pageCount(13,6))
# print(pageCount(13,7))
# print(pageCount(16,11))
print(page_count(6,5))
print(pageCount(6,5))

