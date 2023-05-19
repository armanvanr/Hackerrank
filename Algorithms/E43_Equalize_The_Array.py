def equalizeArray(arr):
    n = len(arr)
    uniq = list(set(arr))
    freq = [arr.count(num) for num in uniq]
    return n-max(freq)

# # Soal
# diberikan sebuah array bilangan bulat
# diminta final array berisi banyak item yang sama (satu bilangan saja)
# dengan jumlah deletion seminimal mungkin
# misal, array = [3,2,2,2,2,1,1,2,2,2,] => final = [2,2,2,2,2,2,2]

# # Algoritma
# Buat list berisi unique value
# hitung frekuensi setiap uniq
# jumlah deletion minimum yaitu banyak array mula dikurangi frekuensi maksimum item array tsb
