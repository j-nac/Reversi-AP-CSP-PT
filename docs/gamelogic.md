# How the Game Logic Works

## Board Notation

| | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | -- | --- | --- |
| 0 | 00 | 10 | 20 | 30 | 40 | 50 | 60 | 70 |
| 1 | 01 | 11 | 21 | 31 | 41 | 51 | 61 | 71 |
| 2 | 02 | 12 | 22 | 32 | 42 | 52 | 62 | 72 |
| 3 | 03 | 13 | 23 | 33 | 43 | 53 | 63 | 73 |
| 4 | 04 | 14 | 24 | 34 | 44 | 54 | 64 | 74 |
| 5 | 05 | 15 | 25 | 35 | 45 | 55 | 65 | 75 |
| 6 | 06 | 16 | 26 | 36 | 46 | 56 | 66 | 76 |
| 7 | 07 | 17 | 27 | 37 | 47 | 57 | 67 | 77 |

All board positions are primarily dealt with in the in the form xy.

The entire board can be exported and imported as a string with a notation system I derived from Forsyth–Edwards Notation (FEN). Each row is given from top to bottom separated with a slash `/`. `b` represents a black disk, `w` represents a white disk, and a number like `2` represents the number of empty spaces. Finally, a letter (either `b` or `w`) at the end signifies whose turn it is.

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



## Execute a turn