# 25
import heapq
from collections import defaultdict


class Node:

    def __init__(self, left, right):
        self.right = right
        self.left = left

    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf:

    def __init__(self, ch):
        self.ch = ch

    def walk(self, code, acc):
        code[self.ch] = acc or "0"


def encodeHuffman(fileIn, fileOut):
    filein = open(fileIn, "r")
    textCount = defaultdict(int)
    _s = ""

    for line in filein:
        lt = line
        _s += line
        for chr in lt:
            textCount[chr] += 1

    h = []
    for ch, freq in textCount.items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)

    count = 0
    while len(h) > 1:
        freq1, _cnt1, left = heapq.heappop(h)
        freq2, _cnt2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1

    code = {}
    if h:
        [(_freq, _cnt, root)] = h
        root.walk(code, "")

    filein.close()
    fileout = open(fileOut, "w")

    s = ""
    encode = "".join(code[ch] for ch in _s)
    for ch in sorted(code):
        s += "{}: {}\n".format(ch, code[ch])
    fileout.write(str(len(code)) + "\n")
    fileout.close()
    print("Коэффициент сжатия методом Хаффмана: " + str(len(_s) / len(encode)))

    if encode != "":
        return True
    else:
        return False


def decodeHuffman(fileIn, fileOut):
    filein = open(fileIn, "r")
    textCount = {}

    n = 0
    encode = ""
    i = 0

    for line in filein:
        i += 1
        if i > 1:
            if i <= n + 1:
                lt = line.split(":")
                textCount[lt[0]] = lt[1]
            else:
                encode = line
        elif i == 1:
            n = int(line)

    sx = []
    enc_ch = ""
    for ch in encode:
        enc_ch += ch
        for dec_ch in textCount:
            if textCount[dec_ch] == (" " + enc_ch + '\n'):
                sx.append(dec_ch)
                enc_ch = ""
                break

    filein.close()
    fileout = open(fileOut, "w")
    result = ''.join(sx)

    fileout.write(result)
    fileout.close()

    return True


encodeHuffman("fileIn.txt", "fileOut.txt")
decodeHuffman("fileOut.txt", "fileOut_Haffman.txt")


# 26
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


def my_split(s):
    st = []
    i_before = 0
    i = 1

    if s[len(s) - 1].isdigit():
        s += "a"
    else:
        s += "0"

    while i < len(s):
        if ((not s[i].isdigit()) & s[i - 1].isdigit()) or (s[i].isdigit() & (not s[i - 1].isdigit())):
            st.append(s[i_before:i])
            i_before = i
        i += 1

    return st


def encodeLZ(fileIn, fileOut):
    encodeDict = defaultdict(lambda: (0, ""))
    filein = open(fileIn, "r")
    encode = ""
    dist_ch = ""
    dist_ch_before = ""
    result = ""

    for line in filein:
        encode += line

    filein.close()

    i = 1
    cnt = True

    for ch in encode:

        if cnt:
            encodeDict[ch] = (i, "")
            i += 1
            cnt = False
            continue

        dist_ch_before = dist_ch
        dist_ch += ch

        if encodeDict[dist_ch][0] == 0:
            encodeDict[dist_ch] = (i, dist_ch_before)
            i += 1
            dist_ch = ""

    cnt = True

    d = encodeDict.copy()

    for it in d.items():

        if cnt:
            result += ("0" + str(get_key(d, (1, ''))))
            cnt = False
            continue

        result += str(encodeDict[it[1][1]][0]) + it[0][-1]

    fileout = open(fileOut, "w")
    fileout.write(result)
    fileout.close()

    print("Коэффициент сжатия методом Лемпеля: " + str(len(encode) / len(result)))

    if result != "":
        return True
    else:
        return False


def decodeLZ(fileIn, fileOut):
    decode = ""
    encode = ""
    decodeDict = defaultdict(int)
    filein = open(fileIn, "r")

    for line in filein:
        encode += line

    filein.close()

    st = my_split(encode)

    decodeDict[""] = 0
    it_before = ""
    cnt = 1

    for it in st:

        if it[0].isdigit():
            it_before = it
            continue


        decodeDict[get_key(decodeDict, int(it_before)) + it] = cnt
        cnt += 1
        decode += get_key(decodeDict, int(it_before)) + it

    fileout = open(fileOut, "w")
    fileout.write(decode)
    fileout.close()

    return True


encodeLZ("fileIn.txt", "fileOut_2.txt")
decodeLZ("fileOut_2.txt", "fileOut_LZ.txt")

# Строку abbaaaaaabbccccbbcccccde лучше кодировать методом Хаффмана,
# потому что здесь очень много повторений, а кол-во совпадающих
# подстрок мало, что и показывает, что отношение длины исходной
# строки к закодированной в методе Хаффмана меньше, чем в методе Лемпеля
# Коэффициент сжатия методом Хаффмана: 0.52
# Коэффициент сжатия методом Лемпеля: 0.8125

# Строку aabbbaabbaa лучше кодировать методом Лемпеля, потому
# что в этой строке много совпадающих подстрок

# Коэффициент сжатия методом Хаффмана: 1.0
# Коэффициент сжатия методом Лемпеля: 0.9285714285714286