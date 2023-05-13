import re
def hm(sentence): # 1/15 passed
    arr = sentence.split()
    for word in arr:
        if word.isdigit():
            arr.remove(word)
    print(arr, len(arr))
# hm("11. How many eggs are in a half-dozen, 13?")
# hm("How many eggs are in a half-dozen, 13?")

def hm2(sentence):
    delimiters=["\.", "\,", "\?", "\!"]
    for d in delimiters:
        sentence = re.sub(d, " ", sentence)
    arr = sentence.split()
    count=0
    for word in arr:
        if word.isalpha() or "-" in word:
            count+=1
    print(arr,count)
hm2("11. How many eggs are in a half-dozen, 13?")

    


