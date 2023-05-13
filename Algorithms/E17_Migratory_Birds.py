def migratoryBirds(arr):
    # id:   0, 1, 2, 3, 4
    list = [0, 0, 0, 0, 0]                  # list untuk menampung frekuensi tipe burung 1-5
    max_sight = 0                           # frekuensi maksimum pengamatan tipe burung
    for type in range(1, 6):                # looping setiap tipe burung 1,2,3,4,5
        for idx, bird in enumerate(arr):    # looping seluruh elemen array
            if bird == type:                # cek apakah current element = tipe burung
                list[type - 1] += 1         # jika sama, frekuensi tipe tersebut bertambah satu, loop untuk elemen burung berikutnya
        if list[type - 1] > max_sight:      # cek apakah tipe burung tersebut merupakan paling banyak
            max_sight = list[type - 1]      # jika iya, tipe tersebut menjadi current max, loop lagi untuk tipe burung berikutnya
    bird_id = list.index(max_sight) + 1     # cari di list frekuensi, index mana yang memuat nilai max, id = index + 1
    return bird_id
    # return list                          # return id_bird

2
print(migratoryBirds([1, 1, 1, 1, 3, 2, 3, 2, 4, 3, 4, 4, 4]))

def mig_bird(arr):
    bird_type = [1,2,3,4,5]
    count_list = []
    for type in bird_type:
        count_list.append(arr.count(type)) 
    max_f = max(count_list)
    result = count_list.index(max_f) +1
    return result

print(mig_bird([1, 1, 1, 1, 3, 2, 3, 2, 4, 3, 4, 4, 4]))

# [count_list.append(arr.count(type)) for type in bird_type]
