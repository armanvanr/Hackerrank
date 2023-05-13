import numpy as np

s= [[5, 3, 4],
    [1, 5, 8],
    [6, 4, 2]]

flatten_s = [item for sublist in s for item in sublist]

s1= [[8, 3, 4],
     [1, 5, 9],
     [6, 7, 8]]

#convert list s menjadi array a
a = np.asarray(s)

#sum dari masing-masing baris, kolom, diagonal
rows = a.sum(axis=1)
cols = a.sum(axis=0)
diags = np.asarray([np.trace(a),np.trace(np.fliplr(a))])

#join baris, kolom, diagonal menjadi satu array
con = np.concatenate((rows,cols))
con = np.concatenate((con,diags))

#cek apakah setiap sum nya sama
result = np.all(con==con[0])
if not result:
    print("not same", con)
    same=[item for item in set(flatten_s) if flatten_s.count(item) > 1]
    same_indices=[flatten_s.index(item) for item in set(flatten_s) if flatten_s.count(item) > 1]
    print(same, same_indices, set(flatten_s))
else:
    print("same")
