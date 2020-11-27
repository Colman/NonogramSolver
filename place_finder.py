'''
Authored by Duncan Krammer
2020-11-26
'''
#===============================================================================

def get_row_indices(index):
    '''
    Get row by index
    Args:
            index - index of the row ranging from [0-8]
    Returns:
            The row as an array
    '''
    row = []
    for i in range(index*9, index*9 + 9):
        row.append(i)
    return row

#===============================================================================

def get_col_indices(index):
    '''
    Get col by index
    Args:
            index - index of the col ranging from [0-8]
    Returns:
            The row as an array
    '''
    col = []
    for i in range(9):
        col.append(index + i * 9)
    return col

#===============================================================================
def get_section_indices(index):
    '''
    Get section by index
    Args:
            index - index of the section ranging from [0-8]
    Returns:
            The section as an array sorted row by row
    '''
    section = []
    for i in range(9):
        if index in [0, 3, 6]:
            if i < 3: section.append(index * 9 + i)
            else: section.append(section[i - 3] + 9)

        if index in [1, 4, 7]:
            if i < 3: section.append((index - 1) * 9 + i + 3)
            else: section.append(section[i - 3] + 9)

        if index in [2, 5, 8]:
            if i < 3: section.append((index - 2) * 9 + i + 6)
            else: section.append(section[i - 3] + 9)
        
    return section

    
#===============================================================================

def check_row(board, row_number):
    '''
    Check row for all valid values. If a given cell
    can only contain one value, place that value.
    Args:
            board - the puzzle to be checked
            row_number - the number of the row to be checked,
                         index ranging from 0 - 8
    Returns:
            row_changed - bool value representing whether a value was placed
    '''

    values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    row = get_row_indices(row_number)

    #store value of row before checks
    old_row = board.get_row(row_number)

    #iterate through possible values, from 1 through 9
    for value in values:
        #Container for all the cells a value could possibly occupy
        possible_cells = []

        #iterate through row
        for cell in row:

            #if cell was part of initial configuration, ignore cell
            if cell in board.static_indices: continue

            #check if current value can be placed in current cell
            if board.is_valid_move(cell, value):
                possible_cells.append(cell)

        #if value can only be placed in one cell, place value
        if len(possible_cells) == 1:
            board.set_cell(possible_cells[0], value)

    #store value of row after checks
    new_row = board.get_row(row_number)

    #check if any changes were made during checks
    row_changed = old_row != new_row

    return row_changed

#===============================================================================

def check_col(board, col_number):
    '''
    Check col for all valid values. If a given cell
    can only contain one value, place that value.
    Args:
            board - the puzzle to be checked
            col_number - the number of the col to be checked,
                         index ranging from 0 - 8
    Returns:
            col_changed - bool value representing whether a value was placed
    '''

    values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    col = get_col_indices(col_number)

    #store value of column before checks
    old_col = board.get_col(col_number)

    #iterate through possible values, from 1 through 9
    for value in values:
        
        #Container for all the cells a value could possibly occupy
        possible_cells = []

        #iterate through column
        for cell in col:

            #if cell was part of initial configuration, ignore cell
            if cell in board.static_indices: continue

            #check if current value can be placed in current cell
            if board.is_valid_move(cell, value):
                possible_cells.append(cell)

        #if value can only be placed in one cell, place value
        if len(possible_cells) == 1:
            board.set_cell(possible_cells[0], value)

    #store value of column after checks
    new_col = board.get_col(col_number)

    #check if any changes were made during checks
    col_changed = old_col != new_col

    return col_changed

#===============================================================================

def check_section(board, section_number):
    '''
    Check section for all valid values. If a given cell
    can only contain one value, place that value.
    Args:
            board - the puzzle to be checked
            section_number - the number of the section to be checked,
                             index ranging from 0 - 8
    Returns:
            section_changed - bool value representing whether a value was placed
    '''
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    section = get_section_indices(section_number)

    #store value of section before checks
    old_section = board.get_section(section_number)

    #iterate through possible values, from 1 through 9
    for value in values:
        
        #Container for all the cells a value could possibly occupy
        possible_cells = []

        #iterate through column
        for cell in section:

            #if cell was part of initial configuration, ignore cell
            if cell in board.static_indices: continue

            #check if current value can be placed in current cell
            if board.is_valid_move(cell, value):
                possible_cells.append(cell)

        #if value can only be placed in one cell, place value
        if len(possible_cells) == 1:
            board.set_cell(possible_cells[0], value)

    #store value of column after checks
    new_section = board.get_section(section_number)

    #check if any changes were made during checks
    section_changed = old_section != new_section

    return section_changed

#===============================================================================

def check_all_rows(board):
    '''
    Checks all rows for all valid values, using check_row.
    Places all possible values.
    Args:
            board - the puzzle to be checked
    '''
    did_not_change = [False, False, False, False, False, False, False, False, False]

    #iterate through rows until rows no longer change
    row_changed = [True, True, True, True, True, True, True, True, True]
    while row_changed != did_not_change:
        for row in range(9):
            row_changed[row] = check_row(board, row)

#===============================================================================

def check_all_cols(board):
    '''
    Checks all columns for all valid values, using check_col.
    Places all possible values.
    Args:
            board - the puzzle to be checked
    '''
    did_not_change = [False, False, False, False, False, False, False, False, False]

    #iterate through columns until columns no longer change
    col_changed = [True, True, True, True, True, True, True, True, True]
    while col_changed != did_not_change:
        for col in range(9):
            col_changed[col] = check_col(board, col)

#===============================================================================

def check_all_sections(board):
    '''
    Checks all sections for all valid values, using check_section.
    Places all possible values.
    Args:
            board - the puzzle to be checked
    '''
    did_not_change = [False, False, False, False, False, False, False, False, False]    

    #iterate through sections until sections no longer change
    section_changed = [True, True, True, True, True, True, True, True, True]
    while section_changed != did_not_change:
        for section in range(9):
            section_changed[section] = check_section(board, section)
    return

#===============================================================================

def place_finder(board):
    '''
    Continuously checks all rows, then columns, then
    sections for any possible values that can be placed.
    Breaks when all rows, columns and sections have been
    checked once with no new values being placed on the
    board.
    Args:
            board - the puzzle to be checked
    '''
    
    while(1):

        old_board_state = board.cells

        check_all_rows(board)
        check_all_cols(board)
        check_all_sections(board)

        new_board_state = board.cells

        if old_board_state == new_board_state:
            break

#===============================================================================

    
