def climbingLeaderboard(ranked, player):
    res = []
    for score in player:
        rank_list = []
        ranked.append(score)
        ranked = sorted(list(set(ranked)), reverse=True)
        for i in range(1,len(ranked)+1):
            rank_list.append(i)
        idx = ranked.index(score)
        current_rank = rank_list[idx]
        res.append(current_rank)
    return res

# print(climbingLeaderboard([100, 90, 80, 90], [70, 80, 105]))

# Dikarenakan untuk skor yang sama punya rank yang sama, leaderboard (ranked) itu dibikin jadi set
# looping setiap skor baru dari alice
# untuk setiap skor alice, kita append ke dalam ranked dan kita bikin list ranking nya (1,2,3,dst)
# index = 0,1,2,3,... rank = 1,2,3,4,....
# jadi ada selisih 1 antara index dari rank_list dan ranking aslinya (rank=index+1)
# dari situ bisa didapat rank dari skor alice saat ini, append ke dalam result (res)
# ulangi lalu return res


def climbing_leaderboard(ranked, player):
    res = []
    ranked = sorted(list(set(ranked)), reverse=True)             # urutkan dari skor tertinggi dan tanpa duplikat (unik)
    for score in player:                                         # baca setiap skor alice
        if score in ranked:                                         # jika skor alice ada di leaderboard,
            score_rank = ranked.index(score) + 1                       # rank sekarang = index + 1

        else:                                                       # jika skor alice tidak ada di leaderboard, update leaderboard
            
            difference = lambda ranked: abs(ranked - score)            # ambil skor yang paling mendekati skor alice
            closest = min(ranked, key=difference)
            
            if score > closest:                                     # jika skor alice melebihi score rank 1
                new_index = ranked.index(closest)                   # ambil index nya sebagai index skor alice (index = 0)
            else:                                                   # jika tidak,
                new_index = ranked.index(closest) + 1               # ambil index dari skor terdekat tsb
            
            ranked.insert(new_index, score)                         # masukkan skor terbaru ke dalam leaderboard
            score_rank = ranked.index(score) + 1                    # rank sekarang = index + 1, dari leaderboard yang diupdate
            ranked.remove(score)                                    # buang skor alice dari leaderboard
        
        res.append(score_rank)                                    # append rank dari score sekarang ke dalam result
    return res, ranked                                         #return result (dalam bentuk list)


# print(climbing_leaderboard([100, 90, 80, 90], [70, 80, 105]))

def clim_leaderboard(ranked, player):
    res = []
    ranked = sorted(list(set(ranked)), reverse=True)
    player = sorted(player, reverse=True)
    rank = 0            
    for i in range(len(player)): 
        while rank < len(ranked) and player[i] < ranked[rank]:
            rank +=1
        res.append(rank+1)
    res.reverse()
    return res


print(clim_leaderboard([100, 90, 80, 90], [70, 80, 105]))