# 15
import math


class HammingEncoder:
    def __init__(self, dataBits):
        self.dataBits = dataBits
        self.encoded = ''

    def encode(self, string):
        controlBits = int(math.log(self.dataBits, 2))
        encoded = list()
        controlindex = list()
        accesslist = list()
        stoplist = list()

        for i in range(controlBits + self.dataBits):
            encoded.append('')

        for i in range(controlBits + 1):
            encoded[2 ** i] = 0
        for i in range(controlBits + 1):
            controlindex.append(2 ** i - 1)
        encoded.pop(0)
        encoded.append('')
        encoded.append('')
        for i in range(len(string)):
            for j in range(controlBits + self.dataBits + 1):
                if encoded[j] == '':
                    encoded[j] = string[i]
                    break

        for i in controlindex:
            res = 0
            k = 0
            turn = i + 1
            for j in range(i, len(encoded), turn):
                if k % 2 == 0:
                    accesslist.append(j)
                if k % 2 == 1:
                    stoplist.append(j)
                k += 1
            new_access = set(accesslist)
            for j in range(len(stoplist)):
                for t in range(accesslist[j] + 1, stoplist[j]):
                    new_access.add(t)
            if len(accesslist) > len(stoplist):
                for p in range(accesslist[len(accesslist) - 1], len(encoded)):
                    new_access.add(p)

            for j in new_access:
                res += int(encoded[j])
            if res % 2 == 1:
                encoded[i] = 1

            res = 0
            new_access.clear()
            k = 0
            accesslist.clear()
            stoplist.clear()

        for i in encoded:
            self.encoded += str(i)

    def decode(self, string):
        controlBits = int(math.log(self.dataBits, 2))
        controlindex = list()

        for i in range(controlBits + 1):
            controlindex.appeend(2 ** i + 1)


code = HammingEncoder(16)
code.encode('1010111101001101')
print(code.encoded)
code = HammingEncoder(8)
code.encode('01011001')
print(code.encoded)
