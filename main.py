def check(positions, ocuppied_rows, column):
    global counter
    for i in range(ocuppied_rows):
        counter += 1
        if positions[i] == column or positions[i] - i == column - ocuppied_rows or \
                positions[i] + i == column + ocuppied_rows:
            return False
    return True


class Queens:
    def __init__(self):
        self.size = 8
        self.solutions = 0
        self.solve()

    def solve(self):
        positions = [-1] * self.size
        self.place_queen(positions, 0)
        print("Найдено решений: ", self.solutions)

    def place_queen(self, positions, target_row):
        if target_row == self.size:
            self.show_board(positions)
            self.solutions += 1
        else:
            for column in range(self.size):
                if check(positions, target_row, column):
                    positions[target_row] = column
                    self.place_queen(positions, target_row + 1)

    def show_board(self, positions):
        for row in range(self.size):
            line = ""
            for column in range(self.size):
                if positions[row] == column:
                    line += "Ф "
                else:
                    line += ". "
            print(line)
        print("\n")


if __name__ == "__main__":
    counter = 0
    Queens()
    print("переборов - ", counter)
