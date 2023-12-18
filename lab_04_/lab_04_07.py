# 16
import math


class Row:
    count = 0

    def __new__(cls, *args, **kwargs):
        cls.count += 1
        return super().__new__(cls)

    def __init__(self, collections, value):
        self.collections = collections
        self.value = value
        self.id = Row.count


class Table:
    def __init__(self, rows_num):
        self.rows_num = rows_num
        self.rows = list()
        var_num = int(math.log2(self.rows_num - 1) + 1)
        s = 0
        for i in range(self.rows_num):
            collections = list(bin(s)[2:var_num + 2].zfill(var_num))
            self.rows.append(Row())
            s += 1

    def add_row(self, row):
        if self.__exist_row(row):
            raise Exception("Row already exist")
        self.rows_num += 1
        self.rows.append(row)

    def __exist_row(self, row):
        exist = False
        for i in self.rows:
            if i.id == row.id:
                exist = True
        return exist

    def set_row(self, row):
        for i in range(self.rows_num):
            if self.rows[i].id == row.id:
                self.rows[i] = row
                return
        raise Exception("Row does not exist in table")

    def get_row(self, row_id):
        for row in self.rows:
            if row.id == row_id:
                return row
        return -1

    def display(self):
        for row_ind in range(self.rows_num):
            print(self.rows[row_ind].id, end='\t')
            for i in self.rows[row_ind].collections:
                print(i, end='\t')
            print('|\t', self.rows[row_ind].value)


class LogicFunction:
    def __init__(self, variables_num, table):
        self.variables_num = variables_num
        self.table = table

    def get_table(self):
        return self.table

    def print_table(self):
        self.table.display()

    def get_expression(self):
        pass
