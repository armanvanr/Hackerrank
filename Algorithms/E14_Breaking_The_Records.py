def breakingRecords(scores):
    temp_max = temp_min = scores[0]
    count_max = count_min = 0
    for score in scores:
        if score > temp_max:
            count_max+=1
            temp_max = score
        if score < temp_min:
            count_min+=1
            temp_min = score
    return [count_max, count_min]