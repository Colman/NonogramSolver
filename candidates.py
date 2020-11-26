def initial_candidates(board):
    '''
    Go through cells in order and determine
    which numbers are possible for each cell.
    Runs exactly once.
    Args:
            board - the puzzle to be checked
    Returns:
            candidates - dictionary of possible values per cell
    '''

    candidates = {}
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    '''
     #to track whether board state changed in loop

    #while(not cell_changed):
    '''
    for i in range(81): #iterate through all cells in board
        if i in board.static_indices: continue #ignore preset cells

        candidate_set = set()
        for value in values:
            if board.is_valid_move(i, value):
                candidate_set.add(value)
        candidates[i] = candidate_set

    return candidates

def check_candidates(board, candidates):
    '''
    Iterate through candidates dict. If only
    one possible value, enter that value in
    the puzzle and remove from dictionary.
    Args:
            board - the puzzle to be checked
            candidates - the dictionary of possible values per cell
    Returns:
            board_changed - bool that tracks if a value was entered
    '''

    delete_cells = []
    board_changed = False
    
    #set values in board
    for cell, vals in candidates.items():
        if len(vals) == 1:
            board.set_cell(cell, vals.pop())
            delete_cells.append(cell)
            board_changed = True

    
    for cells in delete_cells:
        candidates.pop(cells)

    return board_changed


def update_candidates(board, candidates):
    '''
    Updates candidates assuming the board state has changed.
    Args:
            board - the puzzle to be checked
            candidates - the dictionary of possible values per cell
    Returns:
            candidates - the updated dictionary of possible values per cell
            updated - bool value of whether the dict was updated or not
    '''

    
    updated_candidates = {}
    for cell, values in candidates.items(): #iterate through current candidates
        value_set = set()
        for val in values:
            if not board.is_valid_move(cell, val):
                continue
            else:
                value_set.add(val)
        updated_candidates[cell] = value_set

    updated_bool = not updated_candidates == candidates #True if no updates made
    
    return updated_candidates, updated_bool
    

def exhaust_candidates(board):
    '''
    Checks possible cell values, sets guaranteed
    values and updates possible cell values until
    updates no longer happen.
    Args:
            board - the puzzle to be checked
    Returns:
            candidates - the final dictionary of possible values per cell
    '''
    candidates_updated = True
    board_changed = True
    
    candidates = initial_candidates(board)

    #board_updates = 0
    while board_changed:
        board_changed = check_candidates(board, candidates)
        #if not board_changed: print("Final board:")
        #board.print()
        candidates, candidates_updated = update_candidates(board, candidates)
        #board_updates += 1
    #print("Board updates: ", board_updates)


    return candidates













