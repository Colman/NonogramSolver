import tkinter as tk
from board import Board
from brute import Brute
import time

#COlOURS
BASE = "#FFC0CB" #pink
SUDOKU_CLICK = "#ffe4e1"
OPTION_CLICK = "#f78fa7"
STATIC_INDICES = "#fbcce7"
WRONG_MOVE = "#c32148"

#NUMBER-SIZE
NUM_SIZE = 22
BUTTON_TEXT_SIZE = 12


board = Board()
board.parse_board("boards/hard.txt")
# print(board.get_cells()[:30])
cells = []

for section in range(9):
    cells.extend(board.get_section(section))
# print(cells[:30])


def play_move(loc, val, board):
    indices = [] #to preserve indeces cause i'm too tired to do math
    for i in range(81):
        indices.append(i)
    tmp_board = Board(indices)
    updated_indeces = []
    for section in range(9):
        updated_indeces.extend(tmp_board.get_section(section))
    loc_index = updated_indeces.index(loc)
    board.play_move(loc_index,int(val))


# -------- EVENT HANDLING --------
active_option = None
cell_history = []
option_history = []

def handle_cell_click(cells_location, digit, board):
    global active_option
    global cell_history
    if len(cell_history) != 0:
        cell_history[0].config(bg=BASE)
        cell_history.pop()
    digit.config(bg=SUDOKU_CLICK)
    cell_history.append(digit)
    if active_option is not None:
        if active_option == "*":
            digit.config(text=active_option)
        else:
            try:
                play_move(cells_location, active_option, board)
                digit.config(text=active_option)
            except Exception:
                digit.config(bg=WRONG_MOVE)            

def handle_option_click(option):
    global active_option
    global option_history
    if len(option_history) != 0:
        option_history[0].config(bg=BASE)
        option_history.pop()
    option.config(bg=OPTION_CLICK)
    option_history.append(option)
    active_option = option["text"]

def handle_play_button_click(event):
    frm_play_sudoku.grid()
    frm_play_choice_btns.grid()
    frm_solve_sudoku.grid_forget()
    btn_solve.grid_forget()

def handle_solver_button_click(event):
    frm_play_sudoku.grid_forget()
    frm_play_choice_btns.grid_forget()
    frm_solve_sudoku.grid()
    btn_solve.grid(padx=1, pady=3, sticky="nsew")

def handle_how_to_button_click():
    toplevel = tk.Toplevel()
    lbl_how_to = tk.Label(
        master=toplevel,
        text="herro", ####ADDDD HOWWW TOO TEXT HEEEEREEEEEE
        font=("Courier", 16),
        height=0,
        width=50,
        bg=SUDOKU_CLICK,
        fg=WRONG_MOVE,
        padx=10, 
        pady=10,
    )
    lbl_how_to.grid(row=0, column=0, sticky="nsew")

def handle_solve_button_click():
    cells = []
    gui_board = window.grid_slaves()[1]
    for section in reversed(range(9)):
        gui_section = gui_board.grid_slaves()[section]
        for digit in reversed(range(9)):
            gui_digit = gui_section.grid_slaves()[digit]
            val = gui_digit.pack_slaves()[0].get()
            if val == '':
                cells.append('*')
            else:
                cells.append(int(val))
    board = Board(cells)
    cells = []
    for section in range(9):
        cells.extend(board.get_section(section))
    board = Board(cells)

    brute = Brute(board)
    start = time.time()
    brute.solve()
    end = time.time()

    print_board(board, cells, frm_solve_sudoku)

def label_setup(frm_section, board, count):
    global cells
    
    if cells[count] != "*":
        lbl_digit = tk.Label(
            master=frm_section,
            bg=STATIC_INDICES,
            text=f'{cells[count]}',
            font=("Courier", NUM_SIZE),
            width=2
        )
    else:
        lbl_digit = tk.Label(
            master=frm_section,
            bg=BASE, 
            text="",
            font=("Courier", NUM_SIZE),
            width=2
        )
        lbl_digit.bind(
            "<Button-1>", 
            lambda event,
            cells_location=count,
            digit=lbl_digit,
            board=board: 
            handle_cell_click(cells_location, digit, board)
        )

    lbl_digit.pack(fill="both", expand=True)

def entry_setup(frm_section):
    ent_digit = tk.Entry(
        master=frm_section,
        bg=BASE,
        font=("Courier", NUM_SIZE),
        width=2,
        justify='center',
        borderwidth=2,
        relief=tk.FLAT,
    )
    ent_digit.config(
        validate="key", 
        validatecommand=(reg, '%P'),
    )
    ent_digit.pack(padx=1, pady=1, fill="both", expand=True)


def board_setup(frame, option, board):
    #set up board
    for i in range(3):
        for j in range(3):
            frm_board = tk.Frame(
                master=frame,
                relief=tk.GROOVE,
                borderwidth=4,
            )
            frm_board.grid(row=i, column=j, padx=1, pady=1, sticky="nsew")
            #set up sections
            border_w = 1 # for alignment reasons
            if option == 'label':
                border_w = 1
            if option == 'entry':
                border_w = 0
            for ii in range(3):
                for jj in range(3):
                    frm_section = tk.Frame(
                        master=frm_board,
                        relief=tk.FLAT,
                        borderwidth=border_w,
                    )
                    frm_section.grid(row=ii, column=jj, padx=1, pady=1, sticky="nsew")
                    count = 0
                    if option == 'label':
                        label_setup(frm_section, board, count)
                        count += 1
                    if option == 'entry':
                        entry_setup(frm_section)

                  
def debug_nesting(window):
    e = window.grid_slaves()
    print(e,'\n')
    e = e[1].grid_slaves()
    print(e,'\n')
    e = e[0].grid_slaves()
    print(e,'\n')
    e = e[0].pack_slaves()
    # [0].get()
    print(e,'\n')
    
window = tk.Tk()
window.title("Play Sudoku")
window.grid_columnconfigure(0, weight=1) #resizing horizontally

def validate_digit(input):
    '''
    Ensures user input for the solver is valid sudoku symbols.
    Args:
        input - user input
    Returns:
        bool - True if valid input, False if not.
    '''
    if input.isdigit() and len(input) < 2 and input != "0" :
        return True
    elif input == '*':
        return True
    elif input == '':
        return True
    else:
        return False

reg = window.register(validate_digit)

frm_buttons = tk.Frame(
    master=window,
    relief=tk.FLAT,
    borderwidth=1,
)

btn_play = tk.Button(
    master=frm_buttons,
    text="PLAY",
    font=("Courier", BUTTON_TEXT_SIZE),
    bg=BASE,
)

btn_play.bind(
    "<Button-1>",
    handle_play_button_click,
)

btn_play.grid(row=0, column=0, padx=10, pady=10)

btn_solver = tk.Button(
    master=frm_buttons,
    text="SOLVER",
    font=("Courier", BUTTON_TEXT_SIZE),
    bg=BASE,
)

btn_solver.bind(
    "<Button-1>",
    handle_solver_button_click,
)

btn_solver.grid(row=0, column=1, padx=10, pady=10)

btn_how_to = tk.Button(
    master=frm_buttons,
    text="HOW TO",
    font=("Courier", BUTTON_TEXT_SIZE),
    bg=BASE,
    command=handle_how_to_button_click,
)

btn_how_to.grid(row=0, column=2, padx=10, pady=10)

frm_buttons.grid()

frm_play_sudoku = tk.Frame(
    master=window,
    relief=tk.FLAT,
    borderwidth=1,
)

board_setup(frm_play_sudoku ,"label", board)

frm_play_sudoku.grid()

frm_play_choice_btns = tk.Frame(
    master=window,
    relief=tk.FLAT,
    borderwidth=1,
)

counter = []
c = 0
for i in range(9):
    counter.append(i+1)
counter.append('')

for i in range(2):
    for j in range(5):
        frm_choices = tk.Frame(
            master=frm_play_choice_btns,
            relief=tk.GROOVE,
            borderwidth=4,
        )
        frm_choices.grid(row=i, column=j, padx=1, pady=1, sticky="nsew")
        lbl_option = tk.Label(
            master=frm_choices,
            bg=BASE,
            text=f'{counter[c]}',
            font=("Courier", NUM_SIZE),
            width=2
        )
        lbl_option.bind(
            "<Button-1>", 
            lambda event,
            option=lbl_option: 
            handle_option_click(option)
        )
        lbl_option.pack(fill="both", expand=True)
        c += 1

frm_play_choice_btns.grid(pady=3,sticky='')

frm_solve_sudoku = tk.Frame(
    master=window,
    relief=tk.FLAT,
    borderwidth=1,
)

board_setup(frm_solve_sudoku, 'entry', board)

frm_solve_sudoku.grid_forget()
# frm_solve_sudoku.grid()

btn_solve = tk.Button(
    master=window,
    text="SOLVE",
    font=("Courier", BUTTON_TEXT_SIZE),
    bg=BASE,
    command=handle_solve_button_click,
)

btn_solve.grid_forget()
# btn_solve.grid()

window.mainloop()

