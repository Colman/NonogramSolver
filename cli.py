import time


class Cli:
	def __init__(self, board, solver):
		self.board = board
		self.solver = solver


	def start(self):
		while True:
			cmd = input("Please enter a move (ex. B3 2), \"solve\", or \"show\": ")
			if cmd == "solve":
				start = time.time()
				try:
					self.solver.solve()
				except:
					print("Unsolvable from here")
					continue

				end = time.time()
				print("")
				print("Solved in: {:f} seconds".format(end - start))
				self.board.print()
				break

			elif cmd == "show":
				self.board.print()

			else:
				cmds = cmd.split(" ")
				if len(cmds) == 2:
					index = self.board.get_index_from_label(cmds[0])
					if index == -1:
						print("Invalid move1")

					else:
						try:
							value = int(cmds[1])
							self.board.play_move(index, value)
						except:
							print("Invalid move2")
							return

				else:
					print("Invalid move3")

