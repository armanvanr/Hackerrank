import numpy as np
from itertools import combinations


def acmTeam(topic):
    attendee = range(len(topic))
    pairs = []
    max = 0
    count = 1
    for i, a in enumerate(attendee):
        for b in attendee[i + 1 :]:
            known = ""
            for x in range(len(topic[a])):
                known += str(int(topic[a][x]) or int(topic[b][x]))
            val1 = known.count("1")
            print("val1", val1)
            if val1 > max:
                max = val1
                count = 1
            elif val1 == max:
                count += 1
            pairs.append(known)
    return [max, count]


def acmTeam2(topic):
    topic = [int("0b" + topic[i], base=2) for i in range(len(topic))]
    topic = topic[len(topic) // 2 :]
    attendee = range(len(topic))
    res = [
        np.binary_repr(np.bitwise_or(topic[a], topic[b]))
        for i, a in enumerate(attendee)
        for b in attendee[i + 1 :]
    ]
    res.sort(reverse=True)
    max_known = max(res).count("1")
    num_max = res.count(max(res))
    return [max_known, num_max, res]


def acmTeam3(topic):
    topic = [int("0b" + topic[i], base=2) for i in range(len(topic))]
    combs = list(combinations(topic, 2))
    pairs = np.asanyarray(combs)
    res = 0
    for pair in pairs:
        res+=(np.binary_repr(np.bitwise_or(pair[0], pair[1])) )
    return [res]


# print(acmTeam(['10101','11110','00010']))
# print(acmTeam2(['10101','11110','00010']))
print(acmTeam3(["10101", "11100", "11010", "00101"]))
