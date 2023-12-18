# 8 пункт
'''
Логические операции
'''
f = True
g = False
print("f: ", f)
print("not f: ", not f)
print("f and g: ", f and g)
print("f or g: ", f or g)
print("f == g: ", f == g)
print("f != g: ", f != g)
print("\n")
h = 3
i = 5
print("h = ", h)
print("i = ", i)
print("h > i: ", h > i)
print("h < i: ", h < i)
print("h >= i: ", h >= i)
print("0 < h <= i: ", 0 < h <= i)
print("\n")

'''
Побитовые операции
'''
j = 7
k = 20
print("j = %d; j in binary format: %s" % (j, bin(j)))
print("k = %d; k in binary format: %s" % (k, bin(k)))
print("j & k: %d; binary: %s" % (j & k, bin(j & k))) # побитовое AND
print("j | k: %d; binary: %s" % (j | k, bin(j | k))) # побитовое OR
print("j ^ k: %d; binary: %s" % (j ^ k, bin(j ^ k))) # побитовое XOR
print("~k: %d; binary: %s" % (~k, bin(~k)))  # инверсия двоичного числа
print("k>>1: %d; binary: %s" % (k >> 1, bin(k >> 1)))  #сдвиг на один бит вправо
print("k<<1: %d; binary: %s" % (k << 1, bin(k << 1)))  # сдвиг на один бит влево
print("\n")

# 9 пункт
A = 13
B = 5
C = True
D = False

print("A: ", A)
print("B: ", B)
print("C: ", C)
print("D: ", D)
print("\n")

# 10 пункт
print(" ¬ (C ^ D):", not (C and D))
print("C ^ D ∨ ¬ (C ^ D):", C and D or not (C and D))
print("¬ C ∨ D:", not C or D)
print("\n")

# 11 пункт
print("A <= B:", A <= B)
print("A>B ∨ A==B:", A>B or A==B)
print("¬(A<B):", not (A<B))
print("\n")

# 12 пункт
s = 154
p = 6
print("s = %d; s in binary format: %s" % (s, bin(s)))  # s в десятичном и в двоичном виде
print("p = %d; p in binary format: %s" % (p, bin(p)))  # p в десятичном и в двоичном виде
print("\n")

# 13 пункт
s = s | p
print("Результат в десятич.виде s= %d" % s)
b = bin(s)
print("Результат в двоичном виде s= %s" % b)
print("\n")

# 14 пункт
s = s >> 2
print("Результат в десятич.виде s= %d" % s)
s1 = bin(s)
print("Результат в двоичном виде s1= %s" % s1)

p = p >> 2
print("Результат в десятич.виде p= %d" % p)
p1 = bin(p)
print("Результат в двоичном виде p1= %s" % p1)
print("\n")

