def hurdleRace(k, height):
    if max(height)>k:
        return max(height)-k
    else:
        return 0
    