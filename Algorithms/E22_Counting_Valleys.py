def countingValleys(steps, path):
    sign, last_sign = 1, 1
    sign_change, height = 0, 0
    for p in path:                          # looping untuk membaca setiap karakter dari parameter path
        if p == "D":                        # rumpun if else untuk menghitung ketinggian pendaki dari permukaan air
            height -= 1                     # jika D, ketinggian pendaki berkurang satu
        else:
            height += 1                     # jika U, ketinggian pendaki bertambah satu

        if height < 0:                      # rumpun if else untuk menentukan tanda plus atau minus
            sign = -1                       # untuk ketinggian negatif tandanya plus
        else:
            sign = 1                        # untuk ketinggian nol dan positif tandanya plus

        if sign != last_sign:               # rumpun if else untuk 
            sign_change += 1                # menghitung berapa kali tanda tsb berubah
            last_sign = sign                # serta memperbarui tanda
    
    return sign_change//2                   # return total perubahan tanda dibagi 2


print(countingValleys(8, "UDDDUDUU"))
                          