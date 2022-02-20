from itertools import product

a = product(range(2), repeat=25)


class Bingo:
    def __init__(self):
        self.cur = next(a)
        self.answer_count = 0

    def next(self):
        self.cur = next(a)

    def check_diag_up(self):
        for i in range(5):
            if self.cur[((4-i)*5 + i)] != 1:
                return False
        return True

    def check_diag_down(self):
        for i in range(5):
            if self.cur[(i + i*5)] != 1:
                return False
        return True

    def check_part_of_bingo(self, x, y):
        if x == y:
            return self.check_bingo_col(y) or self.check_bingo_row(x) or self.check_diag_down()
        elif 4-x == y:
            return self.check_bingo_col(y) or self.check_bingo_row(x) or self.check_diag_up()
        else:
            return self.check_bingo_col(y) or self.check_bingo_row(x)

    def check_bingo_col(self, y):
        for col in range(5):
            if self.cur[i+y*5] == 0:
                return False
        return True

    def check_bingo_row(self, x):
        for row in range(5):
            if self.cur[x + row * 5] == 0:
                return False
        return True

    def check_sum(self, num):
        return num >= sum(self.cur)

    def check_color(self, x, y):
        return self.cur[x+y*5] == 1

    def check(self):
        line_check = True
        if line_check and
        return self.cur

bingo = Bingo()

for i in range(10):
    print(bingo.check())
    bingo.next()
