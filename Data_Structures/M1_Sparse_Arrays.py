def matchingStrings(stringList, queries):
    res = [stringList.count(q) for q in queries]
    return res