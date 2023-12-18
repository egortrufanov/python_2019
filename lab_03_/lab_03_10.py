# 24
textDict = {}
words = []

f1 = open("text1.txt", "r")
for line in f1:
    words += line.lower().split()
f1.close()

for word in words:
    if word not in textDict:
        textDict[word] = words.count(word)

f2 = open("textDict.txt", 'w')
f2.write(str(textDict))
f2.close()
