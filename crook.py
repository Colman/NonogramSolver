'''
Authored by Duncan Krammer
2020-11-26
'''
#===============================================================================

import candidates
import place_finder

def crook_incomplete(board):
    '''
    Uses the candidate method and place finder method
    alternately to fill in a sudoku puzzle. Stops either
    when a solution is found or no more possible values
    can be filled with these two methods.
    Args:
            board - the puzzle to be checked
    '''

    while(1):
        old_board_state = board.cells

        #Use candidate method to place possible values
        candidates.exhaust_candidates(board)
        cand_board_state = board.cells

        #Check if all cells are filled
        if '*' in cand_board_state: break

        #Use place finder method to place possible values
        place_finder.place_finder(board)
        pf_board_state = board.cells
        
        #Check if all cells are filled
        if '*' in pf_board_state: break

        #Break if no changes were made
        if (old_board_state == cand_board_state) and (old_board_state == pf_board_state):
            break
