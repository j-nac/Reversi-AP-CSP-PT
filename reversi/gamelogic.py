from curses.ascii import isdigit
from re import L


class Board:
    def __init__(self, color='b', srn='8/8/8/3wb3/3bw3/8/8/8 b', turn='b'):
        self.generate_board(srn)
        self.update_score()

    def generate_board(self, srn):
        nboard, self.turn = srn.split()
        
        rows = nboard.split('/')
        board = [[] for x in range(8)]
        for i, row in enumerate(rows):
            for char in row:
                if char.isdigit():
                    for a in range(int(char)):
                        board[i].append(0)
                elif char == 'b':
                    board[i].append(1)
                elif char == 'w':
                    board[i].append(2)
        
        self.board = board

    def get_srn(self):
        pass

    def get_legal_positions(self, move):
        # For every 0, if up, down, left, or right is opp color, go down the row find same color
        pass

    def move(self, move):
        pass

    def update_score(self):
        self.empty_count = sum([row.count(0) for row in self.board])
        self.black_count = sum([row.count(1) for row in self.board])
        self.white_count = sum([row.count(2) for row in self.board])

b = Board()
print(b.empty_count)