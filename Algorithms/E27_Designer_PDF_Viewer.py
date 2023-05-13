def designerPdfViewer(h, word):
    ABC = "abcdefghijklmnopqrstuvwxyz"
    dic = {}
    for i in range(0, 26):
        dic[ABC[i : i + 1]] = h[i]
    tallest = 0
    for alp in word:
        if dic[alp] > tallest:
            tallest = dic[alp]
    area = tallest * len(word)
    return area


h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
print(designerPdfViewer(h, "zaba"))


def designer_pdf_viewer(h, word):
    tallest = 0
    for alp in word:
        index = ord(alp) - 97
        if h[index] > tallest:
            tallest = h[index]
    area = tallest * len(word)
    return area

print(designer_pdf_viewer(h, "zaba"))
