

class Board:
	cells = [] #1d array that stores values row by row


	def __init__(self):
		for i in range(81):
			self.cells.append("*")


	def setCell(self, index, value):
		self.cells[index] = value



	def setCellByLabel(self, label, value):
		index = self.getIndexFromLabel(label)
		self.setCell(index, value)



	def getIndexFromLabel(self, label):
		letters = "ABCDEFGHI"
		col = letters.find(label[0])
		return int(label[1]) * 9 + col



	def getRow(self, index):
		return self.cells[index * 9:index * 9 + 9]



	def getCol(self, index):
		col = []
		for i in range(9):
			col.append(self.cells[index + i * 9])

		return col



	def getSection(self, index):
		topLeft = None
		if index < 3:
			topLeft = index * 3

		elif index < 6:
			topLeft = (index - 3) * 3 + 27

		else:
			topLeft = (index - 6) * 3 + 54

		section = []
		section.extend(self.cells[topLeft:topLeft + 3])
		section.extend(self.cells[topLeft + 9:topLeft + 12])
		section.extend(self.cells[topLeft + 18:topLeft + 21])

		return section



	def isValidMove(self, index, value):
		old = self.cells[index]
		self.setCell(index, value)

		valid = True
		for i in range(9):
			row = self.getRow(i)
			if not self.isUnique(row):
				valid = False
				break

			col = self.getCol(i)
			if not self.isUnique(col):
				valid = False
				break

			section = self.getSection(i)
			if not self.isUnique(section):
				valid = False
				break
			

		self.setCell(index, old)
		return valid



	@staticmethod
	def isUnique(arr):
		vals = []
		for x in arr:
			if x != "*":
				vals.append(x)

		#If all different
		return len(vals) == len(set(vals))


	def print(self):
		print("")
		print("    A B C   D E F   G H I")
		print("  |-------|-------|-------|")

		for i in range(9):
			row = self.getRow(i)
			rowStr = str(i) + " | "

			for j in range(3):
				section = row[j * 3:j * 3 + 3]
				rowStr += " ".join(str(x) for x in section)
				rowStr += " | "

			print(rowStr)

			if i == 2 or i == 5 or i == 8:
				print("  -------------------------")

		print("")
