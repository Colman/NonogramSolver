class Solver:
	board = None
	index = 0

	def __init__(self, board):
		self.board = board



	def solve(self):
		self.index = 0
		while True:
			current = self.board.getCell(self.index)
			if current == "*":
				current = 1
			else:
				current += 1

			while True:
				try:
					self.board.playMove(self.index, current)
					break

				except Exception:
					current += 1
					if current == 10:
						break

			#No possible moves
			if current == 10:
				self.board.playMove(self.index, "*")
				if not self.backTrack():
					raise Exception("Unsolvable board")

			else:
				if not self.frontTrack():
					return



	def frontTrack(self):
		self.index += 1

		while self.index in self.board.staticIndices:
			self.index += 1

		if self.index == 81:
			return False

		return True



	def backTrack(self):
		self.index -= 1

		while self.index in self.board.staticIndices:
			self.index -= 1

		if self.index == -1:
			return False

		return True
			