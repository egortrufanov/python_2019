# 14
import itertools
a = input("Type something: ")
for i in range(len(a)):
    s = set(itertools.permutations(a, i + 1))
    for k in s:
        result = ''
        for j in k:
            result = result + j
        print(result, end=' ')
    print("")
