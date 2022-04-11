# How the Game Logic Works

## Board Notation

| | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | -- | --- | --- |
| 0 | (0, 0) | (1, 0) | (2, 0) | (3, 0) | (4, 0) | (5, 0) | (6, 0) | (7, 0) |
| 1 | (0, 1) | (1, 1) | (2, 1) | (3, 1) | (4, 1) | (5, 1) | (6, 1) | (7, 1) |
| 2 | (0, 2) | (1, 2) | (2, 2) | (3, 2) | (4, 2) | (5, 2) | (6, 2) | (7, 2) |
| 3 | (0, 3) | (1, 3) | (2, 3) | (3, 3) | (4, 3) | (5, 3) | (6, 3) | (7, 3) |
| 4 | (0, 4) | (1, 4) | (2, 4) | (3, 4) | (4, 4) | (5, 4) | (6, 4) | (7, 4) |
| 5 | (0, 5) | (1, 5) | (2, 5) | (3, 5) | (4, 5) | (5, 5) | (6, 5) | (7, 5) |
| 6 | (0, 6) | (1, 6) | (2, 6) | (3, 6) | (4, 6) | (5, 6) | (6, 6) | (7, 6) |
| 7 | (0, 7) | (1, 7) | (2, 7) | (3, 7) | (4, 7) | (5, 7) | (6, 7) | (7, 7) |

All board positions are primarily dealt with in the in the form xy.

The entire board can be exported and imported as a string with a notation system derived from Forsyth–Edwards Notation (FEN) which is named Short Reversi Notation (SRN). Each row is given from top to bottom separated with a slash `/`. `b` represents a black disk, `w` represents a white disk, and a number like `2` represents the number of empty spaces. Finally, a letter (either `b` or `w`) at the end signifies whose turn it is.

The starting position in Reversi can be represented with the string:
`8/8/8/3wb3/3bw3/8/8/8 b`.

While the notation system described above is helpful to efficiently communicate the board position, the board is stored in the form of a list of 8 inner lists containing the piece in each position. `0` is an empty space, `1` is black, and `2` is white.

The starting position in Reversi is shown below:
```
Board.board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 1, 0, 0, 0],
    [0, 0, 0, 1, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]
```

## Get Legal Turns

The number of "flips" are determined with the check_move_flips method. It checks each direction at a time first if there is the opposite color adjacent then for the anchor. If there is at least one flip, it is a legal move.

The get_legal_moves method iterates through each empty square to determine legal moves.

## Execute a turn

The check_move_flips method is run again (an inefficiency I don't care to fix) to get the coordinates for flips then updates the board to reflect the flips.

## Bot Play

The current bot simply gets and executes random legal moves.
