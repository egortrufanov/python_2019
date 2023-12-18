# 15 пункт
'''
Форматированный ввод/вывод данных
'''
m = 10
pi = 3.1415927
print("m = ", m)
print("m = %d" % m)
print("%7d" % m)
print("pi = ", pi)
print("%.3f" % pi)
print("%10.4f\n" % pi)
print("m = {}, pi = {}".format(m, pi))
ch = 'A'
print("ch = %c" % ch)
s = "Hello"
print("s = %s" % s)
print("\n\n")

code = input("Enter your position number in group: ")
n1, n2 = input("Enter two numbers splitted by space:").split()
d, m, y = input("Enter three numbers splitted by \'.\': ").split('.')
print("{} + {} = {}".format(n1,n2,float(n1)+float(n2)))
print("Your birthday is %s.%s.%s and you are %d in the group list" % (d,m,y,int(code)))
print("\n")

# 16 пункт
m = int(input("Введите целочисленное значение m = "))
pi = float(input("Введите вещественное значение pi = "))
print("m = %4d" % m)
print("pi = %.3f" % pi)
print("\n")

# 17 пункт
m = input("Введите число ")
pi = input("Введите число ")
print("m = {}, pi = {}".format(m, pi))
print("\n")

# 18 пункт
year = input("Введите год обучения ")
print("Год Вашего обучения - ", year)
print("\n")

# 19 пункт
m1, r1, p1 = input("Введите результаты ЕГЭ по математике, русскому языку и профильному предмету через , ").split(',')
print(m1, r1, p1)
print("\n")

# 20 пункт

f = input("Введите значение двенадцатизначного шестеричного f = ")
print(int(f, 14 % 8+2))
print("\n")

# 21 пункт
t = int(input("Введите число t = "))
t1 = t << 1
print("t1 = ", t1)
t2 = t >> 1
print("t2 = ", t2)