# 16
num = input("Enter a number: ")
num = int(num, 12)
num1 = ''
while num > 0:
    i = num % 14
    if i == 10:
        i = 'A'
    elif i == 11:
        i = 'B'
    elif i == 12:
        i = 'C'
    elif i == 13:
        i = 'D'
    num1 += str(i)
    num = int(num / 14)
for i in reversed(num1):
    print(i, end='')
