def viralAdvertising(n):
    shared = 5
    cum_liked = 0
    for day in range(n):
        liked = int(shared/2)
        cum_liked += liked
        shared = liked*3
    return cum_liked

viralAdvertising(5)