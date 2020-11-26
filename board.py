class Board:
	'''
	Holds the representation of the board state
	as well as helper functions for making moves,
	getting rows, etc.
	'''

	cells = [] #1d array that stores values row by row
	static_indices = [] #Indices of cells that cannot be changed

	def __init__(self, cells=[]):
		if len(cells) == 0 :
			#Blank cells are the * character
			for i in range(81):
				self.cells.append("*")
		else:
			self.cells = cells


	def parse_board(self, path):
		'''
		Parses a board from a txt file.
		Args:
			path - Path to file
		Returns:
			None
		'''

		f = open(path, "r")
		board_str = f.read()
		cells = []
		for c in board_str:
			#Ignore white space and border chars
			try:
				if c == "*":
					cells.append(c)
				else:
					cells.append(int(c))
			except:
				pass

		#Fill in indices that cannot be changed
		self.static_indices = []
		for i in range(len(cells)):
			if cells[i] != "*":
				self.static_indices.append(i)

		self.cells = cells
			


	def get_cell(self, index):
		'''
		Get the value of a cell
		Args:
			index - The index of the cell ranging from [0-80]
		Returns:
			Value of the cell
		'''

		return self.cells[index]



	def set_cell(self, index, value):
		'''
		Sets the value of a cell
		Args:
			index - The index of the cell ranging from [0-80]
			value - The value of the cell ranging from [1-9]
		Returns:
			None
		'''

		self.cells[index] = value



	def set_cell_by_label(self, label, value):
		'''
		Sets the value of a cell using a label
		Args:
			label - Label of the cell. (A0, C3, etc.)
			value - The value of the cell ranging from [1-9]
		Returns:
			None
		'''

		index = self.get_index_from_label(label)
		self.set_cell(index, value)



	def get_index_from_label(self, label):
		'''
		Converts label to index
		Args:
			label - Label of the cell. (A0, C3, etc.)
		Returns:
			The index of the cell ranging from [0-80]
		'''

		letters = "ABCDEFGHI"
		col = letters.find(label[0])
		return int(label[1]) * 9 + col



	def get_row(self, index):
		'''
		Get row by index
		Args:
			index - Index of the row ranging from [0-8]
		Returns:
			The row as an array
		'''

		return self.cells[index * 9:index * 9 + 9]



	def get_col(self, index):
		'''
		Get column by index
		Args:
			index - Index of the column ranging from [0-8]
		Returns:
			The column as an array
		'''

		col = []
		for i in range(9):
			col.append(self.cells[index + i * 9])

		return col



	def get_section(self, index):
		'''
		Get section by index
		Args:
			index - Index of the section ranging from [0-8]
					(Sections are indexed row by row)
		Returns:
			The section as an array sorted row by row
		'''

		top_left = None
		if index < 3:
			top_left = index * 3

		elif index < 6:
			top_left = (index - 3) * 3 + 27

		else:
			top_left = (index - 6) * 3 + 54

		section = []
		section.extend(self.cells[top_left:top_left + 3]) #First row of section
		section.extend(self.cells[top_left + 9:top_left + 12]) #Second row of section
		section.extend(self.cells[top_left + 18:top_left + 21]) #Third row of section

		return section



	def is_valid_move(self, index, value):
		'''
		Tests whether a move is valid
		Args:
			index - Index of the cell ranging from [0-80]
			value - The value of the cell ranging from [1-9]
		Returns:
			True if the move is valid, False otherwise
		'''

		#Check if index is unchangeable
		if index in self.static_indices:
			return False

		old = self.cells[index] #Save old value
		self.set_cell(index, value)

		#Check if every row section and column is valid
		valid = True
		for i in range(9):
			row = self.get_row(i)
			if not self.is_unique(row):
				valid = False
				break

			col = self.get_col(i)
			if not self.is_unique(col):
				valid = False
				break

			section = self.get_section(i)
			if not self.is_unique(section):
				valid = False
				break
			

		self.set_cell(index, old) #Revert move
		return valid



	def play_move(self, index, value):
		'''
		Plays move if valid. Else raises an exception
		Args:
			index - Index of the cell ranging from [0-80]
			value - The value of the cell ranging from [1-9]
		Returns:
			None
		'''

		if not self.is_valid_move(index, value):
			raise Exception("Invalid move")

		self.set_cell(index, value)



	@staticmethod
	def is_unique(arr):
		'''
		Given an array, checks if every value is unique. (Ignores the * char)
		Args:
			arr - Array of values
		Returns:
			True if the elements are unique, False otherwise
		'''

		vals = []
		for x in arr:
			if x != "*":
				vals.append(x)

		#If all different
		return len(vals) == len(set(vals))


	def print(self):
		'''
		Prints the formatted board
		Args:
			None
		Returns:
			None
		'''

		print("")
		print("    A B C   D E F   G H I")
		print("  -------------------------")

		for i in range(9):
			row = self.get_row(i)
			row_str = str(i) + " | "

			for j in range(3):
				section = row[j * 3:j * 3 + 3]
				row_str += " ".join(str(x) for x in section)
				row_str += " | "

			print(row_str)

			if i == 2 or i == 5 or i == 8:
				print("  -------------------------")

		print("")

	def get_cells(self):
		return self.cells
