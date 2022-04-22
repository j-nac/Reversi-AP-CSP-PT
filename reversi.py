import os
import random
import time

class Board:
    def __init__(self, srn='8/8/8/3wb3/3bw3/8/8/8 b'):
        self.generate_board(srn)
        self.update_score()
    
    def __str__(self):
        return '  ' + '  '.join(list('ABCDEFGH')) + '\n' + '\n'.join([str(i+1) + ' ' + '  '.join(['-' if c == 0 else 'B' if c == 1 else 'W' for c in b]) for i,b in enumerate(self.board)])

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

    @staticmethod
    def convert_move_format(move):
        return ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'][move[0]] + str(move[1] + 1)

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
            total = f'Black {self.black_count} - White {self.white_count}'
            if self.black_count > self.white_count:
                return 'Black side wins\n' + total
            elif self.white_count > self.black_count:
                return 'White side wins\n' + total
            else:
                return 'Draw\n' + total
        else:
            return False

def ask_user(question, options):
    while True:
        os.system('cls')
        print(question)
        for i, option in enumerate(options):
            print(f'{i+1}. {option}')
        answer = input('> ')
        try:
            if int(answer) < 1 or int(answer) > len(options):
                raise
            else:
                return int(answer)
        except Exception:
            os.system('cls')
            input(f'You must enter a number from 1 to {len(options)} as your answer.\nHit ENTER to continue')

if __name__ == '__main__':
    os.system('cls')
    board = Board()

    reversi_ascii = '''
===================================================
||\\\\\\\\\\   |||||| \\\\     || ||\\\\\\\\\\   //||||| ||||||
||   ||   ||      \\\\    || ||   ||   ||        ||
||   //   ||       \\\\   || ||   //   \\\\|||\\\\   ||
|||||\\\\   ||        \\\\  || |||||\\\\        ||   ||
||    \\\\  ||         \\\\ || ||    \\\\       ||   ||
||     \\\\ ||||||      \\\\|| ||     \\\\ |||||// ||||||
===================================================
'''

    print(reversi_ascii)
    input('\nHit ENTER to continue')

    os.system('cls')

    mode = ask_user('Select a game mode', ['Single player', 'Two players'])

    side = 1
    while True:
        is_gameover = board.check_gameover()
        if is_gameover:
            print(is_gameover)
            break

        if len(board.get_legal_moves(side)) == 0:
            input('There are no legal moves that can be performed this turn\nHit ENTER to continue\n')
            continue

        ans = ask_user(str(board) + ('\nBlack side\'s turn' if side == 1 else '\nWhite side\'s turn') + '\nWhat do you want to do?', ['Move', 'Get legal moves', 'Give up'])

        if ans == 1:
            while True:
                try:
                    os.system('cls')
                    print(board)
                    raw_move = input('What is your move? Format as XY (Ex. C7)\n> ')
                    if len(raw_move) != 2:
                        raise
                    if raw_move[0] not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
                        raise
                    if int(raw_move[1]) not in [1, 2, 3, 4, 5, 6, 7, 8]:
                        raise
                    move = (['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'].index(raw_move[0]), int(raw_move[1]) - 1)

                    if move not in board.get_legal_moves(side):
                        raise
                    else:
                        break
                except Exception:
                    os.system('cls')
                    input('You must enter a legal move in the form XY as your answer. (Ex. G2)\nHit ENTER to continue')

            board.execute_move(move, side)
            if mode == 1:
                os.system('cls')
                print(board)
                is_gameover = board.check_gameover()
                if is_gameover:
                    print(is_gameover)
                    break
                input('Hit ENTER to continue')
                for x in range(4):
                    os.system('cls')
                    print('CPU deciding' + x*'.')
                    time.sleep(0.5)
                if len(board.get_legal_moves(2)):
                    board.execute_move(random.choice(board.get_legal_moves(2)), 2)
                else:
                    continue
            else:
                side = 1 if side == 2 else 2
        elif ans == 2:
            os.system('cls')
            print(board)
            print(', '.join([board.convert_move_format(m) for m in board.get_legal_moves(side)]))
            input('Hit ENTER to continue')
        elif ans == 3:
            print('Goodbye')
            break