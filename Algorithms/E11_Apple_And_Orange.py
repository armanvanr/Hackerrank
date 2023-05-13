def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_apple, count_orange = 0, 0
    for apple in apples:
        if s<= a+apple <=t:
            count_apple+=1
    for orange in oranges:
        if s<= b+orange <=t:
            count_orange+=1
    print(count_apple)
    print(count_orange)