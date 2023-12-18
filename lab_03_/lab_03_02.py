# 5
'''
Множества
'''
# создание множества
b1 = set()
print("Set b1 = ", b1)
b2 = {"bear", "fox", "squirrel", "woodpecker", "woodpecker", "wolf", "hedgehog"}
print("Set b2 = ", b2)
# создание множества из строки
b3 = set("abcdabcdefg")
print("Set b3 from string: ", set(b3))
print("\n")

# 6
s1 = "Electricity is the set of physical phenomena associated with the presence of electric charge. Lightning is one of the most dramatic effects of electricity"
set1 = set(s1)
print(set1)
print("\n")

# 7
for i in set1:
    j = i.lower()
    if j == 'a' or j == 'i'or j == 'e' or j == 'o' or j == 'u'or j == 'y':
        print(i, end=' ')