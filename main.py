from board import Board
from solver import Solver


board = Board()
board.parseBoard("boards/insane.txt")

solver = Solver(board)
solver.solve()

board.print()