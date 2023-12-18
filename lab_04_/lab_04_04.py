# 12
from collections import Counter


class Encoder:

    def encode(self, string: str):
        pass

    def decode(self, string: str):
        pass


class HuffmanEncoder(Encoder):

    SPLIT_SYMBOL = chr(1)
    END_SYMBOL = chr(12)

    def __init__(self):
        self.compressionCoef = None

    def encode(self, string: str):
        op_dict = Counter(string)
        lt = list(op_dict.most_common(len(op_dict)))
        table = self.__Haf(self.__letter_tree(lt), '')

        encoded = ''
        bits = 0
        for key in table.keys():
            encoded += key + HuffmanEncoder.SPLIT_SYMBOL + table[key] \
                       + HuffmanEncoder.END_SYMBOL
            bits += 3*8 + len(table[key])
        for i in string:
            encoded += table[i]
            bits += 1
        self.__setCompressionCoef(len(string) * 8 / bits)
        return encoded

    def decode(self, string: str):
        f = string.split(HuffmanEncoder.END_SYMBOL)
        table = {i[1 + len(HuffmanEncoder.SPLIT_SYMBOL):]: i[0] for i in f[:-1]}
        code = f[-1]

        cur_seq = ''
        table_seq = list(table.keys())

        decoded = ''

        for symbol in code:
            cur_seq += symbol
            if cur_seq in table_seq:
                decoded += table[cur_seq]
                cur_seq = ''
        return decoded

    def __setCompressionCoef(self, value):
        self.compressionCoef = value

    def getCompressionCoef(self):
        return self.compressionCoef

    def __letter_tree(self, d):

        if len(d) == 1:
            return d[0][0]

        last_pair = d[-1]
        pre_last_pair = d[-2]

        new_el = ((last_pair[0], pre_last_pair[0]), last_pair[1] + pre_last_pair[1])
        del d[-1]
        del d[-1]

        d.append(new_el)
        d.sort(key=lambda x: x[1], reverse=True)

        return self.__letter_tree(d)

    def __Haf(self, tree, code):
        if type(tree) == str:
            return {tree: code}
        d = {}
        d.update(self.__Haf(tree[0], code + '0'))
        d.update(self.__Haf(tree[1], code + '1'))
        return d


class LZEncoder(Encoder):

    def __init__(self):
        self.compressionCoef = 0

    def __setCompressionCoef(self, value):
        self.compressionCoef = value

    def getCompressionCoef(self):
        return self.compressionCoef

    def encode(self, string: str):
        data = string
        encoded = ''

        char_dict = {data[0]: 0}
        counter = 1
        k = [(data[0], 0)]
        cur_chars = ''
        encoded += str(0) + data[0]
        for char in data[1:]:
            new_chars = cur_chars + char
            if new_chars in char_dict:
                cur_chars = new_chars
            else:
                if len(new_chars) == 1:
                    encoded += str(0) + new_chars
                else:
                    encoded += str(char_dict[cur_chars] + 1) + char
                    cur_chars = ''
                char_dict.update({new_chars: counter})
                counter += 1
        else:
            char = ""
            new_chars = cur_chars + char
            if len(new_chars) <= 1:
                encoded += str(0) + new_chars
            else:
                encoded += str(char_dict[cur_chars] + 1) + char
        self.__setCompressionCoef(len(string) / len(encoded))
        return encoded

    def decode(self, string: str):
        data = string
        decoded = ''

        char_dict = {'0': ''}
        counter = 1
        data = self.__get_pairs(data)
        for pair in data:
            new_chars = char_dict[pair[0]] + pair[1]
            char_dict[str(counter)] = new_chars
            decoded += new_chars
            counter += 1
            data = data[len(pair[0]) + 1:]

    def __get_pairs(self, data):
        pairs = []
        ind = ''
        for i in data:
            if i not in '0123456789':
                pairs.append((ind, i))
                ind = ''
            else:
                ind += i
        return pairs


dec = HuffmanEncoder()
print(dec.decode(dec.encode('Python is a widely used high-level programming language for general-purpose \nprogramming, created by Guido van Rossum and first released in 1991')))
print(dec.getCompressionCoef())