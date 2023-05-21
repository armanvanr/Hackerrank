def acmTeam(topic):
    attendee=range(len(topic))
    known = []
    pairs = []
    # pairs = [[a,b] for i, a in enumerate(attendee) for b in attendee[i+1:]]
    for i, a in enumerate(attendee):
        for b in attendee[i+1:]:
            # print(a,b,topic[a], topic[b])
            for x in topic[a]:
                for y in topic[b]:
                    known.append(int(x) or int(y))
            pairs.append([a,b])
    return known


print(acmTeam(['1110','1010','0001']))

