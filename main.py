from board import Board
from brute import Brute
from gui import Gui
import time

file_name = input("What board would you like? (easy/medium/hard/insane): ")
board = Board()
board.parse_board("boards/" + "hard" + ".txt")

ans = input("Would you like to use the GUI? (y/n): ")

brute = Brute(board)
if ans == "y":
	gui = Gui(board, brute)
	gui.start()

else:
	start = time.time()
	brute.solve()
	end = time.time()

	print("")
	print("Solved in: {:f} seconds".format(end - start))
	board.print()