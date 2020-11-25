from board import Board
from brute import Brute
import time


board = Board()
board.parse_board("boards/hard.txt")

brute = Brute(board)
start = time.time()
brute.solve()
end = time.time()

print("")
print("Solved in: {:f} seconds".format(end - start))
board.print()