import tkinter as tk
from tkinter import ttk
from board import Board

#COlOURS
BASE = "#FFC0CB" #pink
SUDOKU_CLICK = "#ffe4e1"
OPTION_CLICK = "#f78fa7"
STATIC_INDICES = "#fbcce7"
WRONG_MOVE = "#c32148"


board = Board()
board.parse_board("boards/hard.txt")
# print(board.get_cells()[:30])
cells = []
count = 0

for section in range(9):
    cells.extend(board.get_section(section))
print(cells[:30])


def play_move(loc, val, board):
    indices = [] #to preserve indeces cause i'm too tired to do math
    for i in range(81):
        indices.append(i)
    tmp_board = Board(indices)
    updated_indeces = []
    for section in range(9):
        updated_indeces.extend(tmp_board.get_section(section))
    # print(updated_indeces[:30])

    # print(board.get_cells()[:30])
    loc_index = updated_indeces.index(loc)
    board.play_move(loc_index,int(val))



# -------- EVENT HANDLING --------
active_option = None
cell_history = []
option_history = []

def handle_cell_click(cells, cells_location, digit, board):
    global active_option
    global cell_history
    if len(cell_history) != 0:
        cell_history[0].config(bg=BASE)
        cell_history.pop()
    digit.config(bg=SUDOKU_CLICK)
    cell_history.append(digit)
    if active_option is not None:
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
    print("play")

def handle_solver_button_click(event):
    print("solver")



window = tk.Tk()
window.title("Play Sudoku")

# frm_buttons = tk.Frame(
#     master=window,
#     relief=tk.FLAT,
#     borderwidth=1,
# )

# btn_play = tk.Button(
#     master=frm_buttons,
#     text="PLAY",
#     font=("Courier", 44),
# )

# btn_play.bind(
#     "<Button-1>",
#     handle_play_button_click,
# )

# btn_play.grid(row=0, column=0)

# btn_solver = tk.Button(
#     master=frm_buttons,
#     text="SOLVER",
#     font=("Courier", 44),
# )

# btn_solver.bind(
#     "<Button-1>",
#     handle_solver_button_click,
# )

# btn_solver.grid(row=0, column=1)


# frm_buttons.pack(padx=5)

frm_sudoku_game = tk.Frame(
    master=window,
    relief=tk.FLAT,
    borderwidth=1,
)

for i in range(3):
    for j in range(3):
        frm_board = tk.Frame(
            master=frm_sudoku_game,
            relief=tk.GROOVE,
            borderwidth=4,
        )
        frm_board.grid(row=i, column=j, padx=1, pady=1, sticky="nsew")
        for ii in range(3):
            for jj in range(3):
                frm_section = tk.Frame(
                    master=frm_board,
                    relief=tk.FLAT,
                    borderwidth=1,
                )
                frm_section.grid(row=ii, column=jj, padx=1, pady=1, sticky="nsew")
                if cells[count] != "*":
                    lbl_digit = tk.Label(
                        master=frm_section,
                        bg=STATIC_INDICES,
                        text=f'{cells[count]}',
                        font=("Courier", 44),
                        width=2
                    )
                else:
                    lbl_digit = tk.Label(
                        master=frm_section,
                        bg=BASE, 
                        text=f'{cells[count]}',
                        font=("Courier", 44),
                        width=2
                    )
                    lbl_digit.bind(
                        "<Button-1>", 
                        lambda event,
                        cells=cells,
                        cells_location=count,
                        digit=lbl_digit,
                        board=board: 
                        handle_cell_click(cells, cells_location, digit, board)
                    )
                count += 1
                lbl_digit.pack( fill="both", expand=True)

frm_sudoku_game.pack()

frm_play_choice_btns = tk.Frame(
    master=window,
    relief=tk.FLAT,
    borderwidth=1,
)

counter = []
c = 0
for i in range(9):
    counter.append(i+1)
counter.append('*')

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
            font=("Courier", 44),
            width=2
        )
        lbl_option.bind(
            "<Button-1>", 
            lambda event,
            option=lbl_option: 
            handle_option_click(option)
        )
        lbl_option.pack()
        c += 1

frm_play_choice_btns.pack(pady=3)

window.mainloop()

