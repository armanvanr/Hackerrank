def libraryFine(d1, m1, y1, d2, m2, y2):
    # since it is guaranteed gregorian calendar for all years,
    # we don't have to worry the jumping dates in the transition year 1918

    fine=0
    # since y1 is before y2, it must be on time
    if y1<y2:
        pass

    # it's probably late, check further 
    elif y1==y2:

        # since m1 is before m2, it must be on time
        if m1<m2:
            pass

        # it's probably late, check further
        elif m1==m2:

            # since d1 is before d2, it's on time
            if d1<=d2:
                pass

            # it's late within the same month
            else:
                fine = (d1-d2)*15

        # it's late within the same year, different month
        else:
            fine = (m1-m2)*500
    
    # it's lateeeeee
    else:
        fine = 10000

    return fine

print(libraryFine(2,7,1014,1,1,1015))

def library_fine(d1, m1, y1, d2, m2, y2):
    if y1<y2 or (y1==y2 and m1<m2) or (y1==y2 and m1==m2 and d1<=d2): return 0
    if y1>y2: return 10000
    if y1==y2 and m1>m2: return (m1-m2)*500
    if y1==y2 and m1==m2 and d1>d2: return (d1-d2)*15
    # Guard Clause technique: ga perlu pake else
