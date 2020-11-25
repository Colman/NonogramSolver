class Brute:
	'''Brute force solver'''

	board = None
	index = 0

	def __init__(self, board):
		self.board = board



	def solve(self):
		'''
		Solves the given board. Raises exception if unsolvable.
		Args:
			None
		Returns:
			None
		'''

		self.index = 0
		while True:
			#Increment current value of cell
			current = self.board.get_cell(self.index)
			if current == "*":
				current = 1
			else:
				current += 1

			#Find the first move that works for that cell
			while True:
				try:
					self.board.play_move(self.index, current)
					break

				except Exception:
					current += 1
					if current == 10:
						break

			#No possible moves
			if current == 10:
				self.board.play_move(self.index, "*")
				if not self.back_track():
					raise Exception("Unsolvable board")

			else:
				#If at the end of the board
				if not self.front_track():
					return



	def front_track(self):
		'''
		Find the next biggest index that isn't static
		Args:
			None
		Returns:
			The index
		'''

		self.index += 1

		while self.index in self.board.static_indices:
			self.index += 1

		if self.index == 81:
			return False

		return True



	def back_track(self):
		'''
		Find the previous biggest index that isn't static
		Args:
			None
		Returns:
			The index
		'''

		self.index -= 1

		while self.index in self.board.static_indices:
			self.index -= 1

		if self.index == -1:
			return False

		return True
			