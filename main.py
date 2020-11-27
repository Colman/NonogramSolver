from board import Board
from brute import Brute
from gui import Gui
from cli import Cli
import crook
import time

board = Board()
ans = input("Select mode (cli/gui/compare): ")

if ans == "cli" or ans == "gui":
	brute = Brute(board)
	file_name = input("What board would you like? (easy/medium/hard/insane): ")
	board.parse_board("boards/" + file_name + ".txt")

	if ans == "cli":
		cli = Cli(board, brute)
		cli.start()

	else:
		gui = Gui(board, brute)
		gui.start()

else:
	board = Board()
	puzzles = ["boards/easy.txt", "boards/medium.txt", "boards/hard.txt", "boards/insane.txt"]

	for puzzle in puzzles:
	    print("======================================================")
	    print(puzzle)
	    print()
	    
	    #Brute force method
	    print("Brute force solution")
	    board.parse_board(puzzle)
	    brute = Brute(board)

	    start = time.time()
	    brute.solve()
	    end = time.time()
	    brute_time = end - start

	    board.print()

	    #Crook method (partial)
	    print("Partial Crook method solution")
	    board.parse_board(puzzle)

	    start = time.time()
	    crook.crook_incomplete(board)
	    end = time.time()
	    crook_time = end - start

	    board.print()

	    #Print results
	    print("Brute time: {:f} seconds".format(brute_time))
	    print("Crook time: {:f} seconds".format(crook_time))
