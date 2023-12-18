# 4
"""
Циклы
"""
# while
print("Numbers < 10 (while):")
i = 0
while i < 10:
    print(i, end=" ")  # print in one line
    i += 1
print("\n")

# for
print("Numbers < 10 (for):")
for i in range(0, 10):
    print(i, end=" ")
else:
    print("\nThe next number is 10\n")

# break
sum = 0
for i in range(0, 100):
    if i > 10:
        print("\nWe reached the end, final sum: ", sum)
        break
    sum += i

# continue
i = 0
while i <= 15:
    if i % 3 == 0:
        i += 1
        continue
    print(i, end=" ")
    i += 1
print("\n")

# pass
print("Let's print numbers again!")
for i in range(0, 10):
    pass
    print(i, end=" ")
print("\n\n")

# 5
for i in range(0, 500):
    if i % 7 == 0:
        print(i)
    i += 1
else:
    print("All numbers were printed!")
print("\n")

i = 0
while i < 501:
    if i % 7 == 0:
        print(i)
    i += 1
else:
    print("All numbers were printed!")
print("\n\n")

# 6
for i in range(0, 500):
    if i >= 300:
        print("All numbers were printed!")
        break
    if i % 7 == 0 and i % 14 == 0:
        print(i)
    i += 1
else:
    print("All numbers were printed!")
print("\n")

i = 0
while i < 501:
    if i >= 300:
        print("All numbers were printed!")
        break
    if i % 7 == 0 and i % 14 == 0:
        print(i)
    i += 1
else:
    print("All numbers were printed!")
print("\n\n")

# 7
for x in range(0, 4):
    for y in range(0, 4):
        if x == y:
            print(x+1, end=" ")
        elif x != y:
            print(0, end=" ")
    print(" ")
print("\n")

x = 0
y = 0
while x < 4:
    while y < 4:
        if x == y:
            print(x + 1, end=" ")
        elif x != y:
            print(0, end=" ")
        y += 1
    print(" ")
    y = 0
    x += 1
print("\n\n")
