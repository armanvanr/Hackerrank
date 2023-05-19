def nd1(name, price, weight):  # 7/13
    arr = []
    uniq = []
    for i in range(len(name)):
        arr.append([name[i], price[i], weight[i]])
    for item in arr:
        if item not in uniq:
            uniq.append(item)
    dups = 0
    for item in uniq:
        n = arr.count(item)
        if n > 1:
            dups += n - 1
    return dups


def nd2(name, price, weight):  # 7/13
    arr = [[name[i], price[i], weight[i]] for i in range(len(name))]
    uniq = []
    for item in arr:
        if item not in uniq:
            uniq.append(item)

    dups = 0
    for item in uniq:
        n = arr.count(item)
        if n > 1:
            dups += n - 1
    return dups


def nd3(name, price, weight):  # ?/13
    uniq = []
    for i in range(len(name)):
        item = [name[i], price[i], weight[i]]
        if item not in uniq:
            uniq.append(item)
    dups = len(name) - len(uniq)
    return dups


if __name__ == "__main__":
    names = ["ball", "box", "ball", "ball", "box"]
    prices  = [2, 2, 2, 2, 2]
    weights = [1, 2, 1, 1, 3]
    print(nd1(names, prices, weights))
    print(nd2(names, prices, weights))
    print(nd3(names, prices, weights))
