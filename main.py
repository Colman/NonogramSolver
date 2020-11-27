from board import Board
from brute import Brute
import time
import crook

'''
Candidate method is generally faster, especially in cases
where the puzzle works against the brute force algorithm
(i.e. the top row contains 1 through 9 in reverse order)
but candidate method does not work for all puzzles, only
for puzzles that can be solved through basic deduction.
Brute force algorithm will always find a solution.

***Candidate method cannot find solutions to the hard or
   insane boards***
'''

board = Board()

board.parse_board("boards/insane.txt")
board.print()

crook.crook_incomplete(board)

board.print()
'''
row_changed = [True, True, True, True, True, True, True, True, True]
row_false = [False, False, False, False, False, False, False, False, False]
while row_changed != row_false:
    for row in range(9):
        row_changed[row] = place_finder.check_row(board, row)
        #board.print()
    
#cand = candidates.exhaust_candidates(board)

board.print()

col_changed = [True, True, True, True, True, True, True, True, True]
col_false = [False, False, False, False, False, False, False, False, False]
while col_changed != col_false:
    for col in range(9):
        col_changed[col] = place_finder.check_col(board, col)
        #board.print()
    
#cand = candidates.exhaust_candidates(board)
'''
#board.print()


'''
board = Board()
puzzles = ["boards/easy.txt", "boards/medium.txt", "boards/hard.txt", "boards/insane.txt"]

for puzzle in puzzles:
    print("======================================================")
    print(puzzle)
    #Brute force method
    board.parse_board(puzzle)
    brute = Brute(board)
    start = time.time()
    brute.solve()
    end = time.time()
    brute_time = end - start
    board.print()

    #Candidate method
    board.parse_board(puzzle)
    start = time.time()
    cand = candidates.exhaust_candidates(board)
    end = time.time()
    board.print()

    cand_time = end - start
    #print("Solved in: {:f} seconds".format(end - start))

    print("Brute time: {:f} seconds".format(brute_time))
    print("Candidate time: {:f} seconds".format(cand_time))

'''






    
