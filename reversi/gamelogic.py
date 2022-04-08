from curses.ascii import isdigit
from re import L


class Board:
    def __init__(self, srn='8/8/8/3wb3/3bw3/8/8/8 b'):
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

    def get_legal_moves(self, color_num: int) -> list:
        legal_moves = []

        for y, row in enumerate(self.board):
            for x, square in enumerate(row):
                if square == 0:
                    coords = (x, y)
                    if self.check_move_flips(coords, color_num):
                        legal_moves.append(coords)
        
        return legal_moves
    

    def check_move_flips(self, coords: tuple, color_num: int) -> list:
        flips = []
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

        if not(color_num == 1 or color_num == 2):
            raise ValueError('color_num must be 1 or 2')
        
        opp_color = ((color_num - 1.5) * -2 + 3) / 2

        for d in directions:
            test_coords = tuple(map(sum, zip(coords, d)))
            if self.is_in_bounds(test_coords):
                test_square = self.board[test_coords[1]][test_coords[0]]
                # Check if opposite color in between
                if test_square != opp_color:
                    continue
                # Find anchor while saving flips
                possible_flips = [test_coords]
                while True:
                    test_coords = tuple(map(sum, zip(test_coords, d)))
                    if self.is_in_bounds(test_coords):
                        test_square = self.board[test_coords[1]][test_coords[0]]
                        if test_square == opp_color:
                            possible_flips.append(test_coords)
                        elif test_square == color_num:
                            flips += possible_flips
                            break
                        else:
                            break
                    else:
                        break
        
        return flips
                    
    def execute_move(self, coords):
        pass

    def update_score(self):
        self.empty_count = sum([row.count(0) for row in self.board])
        self.black_count = sum([row.count(1) for row in self.board])
        self.white_count = sum([row.count(2) for row in self.board])
    
    def is_in_bounds(self, coords):
        for c in coords:
            if c < 0 or c > 7:
                return False
        return True

b = Board()
print(b.get_legal_moves(2))