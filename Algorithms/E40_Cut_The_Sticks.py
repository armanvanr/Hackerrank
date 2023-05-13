def cutTheSticks(arr):
    res = []
    unique = sorted(list(set(arr)))
    freq = []
    for num in unique:
        freq.append(arr.count(num))

    n_arr = len(arr)
    n_uni = len(unique)
    short_idx = 0
    while n_arr > 0:
        res.append(n_arr)
        shortest = unique[short_idx]
        i = 0
        while i < n_uni:
            if unique[i] != 0:
                unique[i] -= shortest
            i += 1
        f0 = freq[short_idx]        
        n_arr -= f0
        short_idx += 1
    return res
a=[5, 4, 4, 2, 2, 8]
print(cutTheSticks(a))


# kita mau ngitung banyak stik sebelum dipotong (number of array elements = n_arr)
# karena diminta kembalikan dalam bentuk array/list yang isinya banyak stik setiap kali iterasi, maka bikin list kosong

# karena yang diminta banyak stik sebelum dipotong, append "n_arr" dulu
# tentukan shortest stick
# looping array stik nya, lakukan pemotongan/decrement ke tiap stik sebanyak 1x sebesar shortest
# "n_arr" terbaru = "n_arr" sebelumnya dikurangi banyak stik yang nol
# append "n_arr" terbaru kedalam list
# update shortest stick
# selama "n_arr" lebih dari nol, lakukan terus loop tsb
# jadi ada dua loop (nested), loop kondisi apakah "n_arr" masih ada? dan loop apakah semua stik sudah terpotong?

# tapi kalo gitu, nanti kita jadi perlu count berkali-kali, mungkin nanti kata HackerRank ga efisien
# jadi aku bikin list unique beserta list freq nya, dan diurutkan dari terkecil
# nanti nilai frekuensinya dipake dalam perhitungan "n_arr" terbaru

# tiap stik dipotong lewat looping, kalo udah habis nilainya nol (bukan negatif!)
# awalnya kepikiran meski udah nol, semua stik tetep dikurangi terus sampe minus, lalu append "n_arr terbaru"
# tapi itu ga efisien, karena udah nol ngapain dikerjain, nambah-nambah beban hidup :)
# jadi akhirnya kalo stik itu udah nol, ga perlu di-decrement lagi, ngurangi iterasi => naikin efisiensi kodingan
