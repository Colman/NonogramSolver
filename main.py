from board import Board

test = Board()
test.setCellByLabel("G3", 6)
test.setCellByLabel("H4", 4)
test.setCellByLabel("I5", 2)
test.print()

print(test.isValidMove(36, 6))