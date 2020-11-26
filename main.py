from board import Board
from brute import Brute
import time
import candidates


board = Board()
board.parse_board("boards/hard.txt")

'''
brute = Brute(board)
start = time.time()
brute.solve()
end = time.time()

print("")
print("Solved in: {:f} seconds".format(end - start))
'''
board.print()


candidates = candidates.exhaust_candidates(board)
print(candidates)
board.print()

'''
for k, v in cand.items():
    if k in new_cand:
        if cand[k] != new_cand[k]:
            print("old vals: ", k, cand[k])
            print("new vals: ", k, new_cand[k])
'''
