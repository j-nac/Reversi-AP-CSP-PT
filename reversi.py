class Board:
    def __init__(self, srn='8/8/8/3wb3/3bw3/8/8/8 b'):
        self.generate_board(srn)
        self.update_score()
    
    def __repr__(self):
        return '\n'.join(['  '.join([str(c) for c in b]) for b in self.board])

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
                    
    def execute_move(self, coords: tuple, color_num: int):
        flips = self.check_move_flips(coords, color_num)
        self.board[coords[1]][coords[0]] = color_num
        for f in flips:
            self.board[f[1]][f[0]] = color_num
        self.update_score()

    def update_score(self):
        self.empty_count = sum([row.count(0) for row in self.board])
        self.black_count = sum([row.count(1) for row in self.board])
        self.white_count = sum([row.count(2) for row in self.board])
    
    def is_in_bounds(self, coords):
        for c in coords:
            if c < 0 or c > 7:
                return False
        return True
    
    def check_gameover(self):
        if not (self.get_legal_moves(1) or self.get_legal_moves(2)):
            if self.black_count > self.white_count:
                return 'Black side wins'
            elif self.white_count > self.black_count:
                return 'White side wins'
            else:
                return 'Draw'
        else:
            return False

if __name__ == '__main__':
    board = Board()
    side = 1
    while True:
        print(board)

        is_gameover = board.check_gameover()
        if is_gameover:
            print(is_gameover)
            break

        ans = int(input('What do you want to do?\n1. Move\n2. Get legal moves\n3. Give up\n> '))

        if ans == 1:
            i = input('What is your move? Format as x,y\n> ').split(',')
            x, y = [int(a) for a in i]
            board.execute_move((x,y), side)
            side = round(((side - 1.5) * -2 + 3) / 2)
        elif ans == 2:
            print(board.get_legal_moves(side))
        elif ans == 3:
            print('Lol')
            break
            
        
        # Switch color: side = ((side - 1.5) * -2 + 3) / 2