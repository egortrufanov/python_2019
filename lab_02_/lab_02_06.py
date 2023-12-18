# 15
num = '0x' + (input("Введите шестнадцатеричное число из восьми разрядов: "))
num1 = '0xFFFFFFFF'
rev_code = hex(int(num, 0) ^ int(num1, 0))
print("Обратный код: %s" % rev_code[2::])
bit = '0x00000001'
add_code = hex(int(rev_code, 0) + int(bit, 0))
print("Дополнительный код: %s" % add_code[2::])
