import tkinter as tk
from tkinter import ttk
from board import Board


class Gui:
    '''
    This class handles the user interface for
    SlickSudoku.
    '''

    #Colors
    BASE = "#ffc0cb"
    SUDOKU_CLICK = "#ffe4e1"
    OPTION_CLICK = "#f78fa7"
    STATIC_INDICES = "#fbcce7"
    WRONG_MOVE = "#c32148"

    #Events
    string_vars = {} #Key: str(index), value: Tkinter string value of each cell

    #Help
    help_str = '''
    Welcome to SlickSudoku! Please enter a digit from 1 to 9 in each of the boxes.
    A number can be played as long as there are no duplicate numbers in the rows,
    columns, or 3x3 sections on the board. To solve the puzzle, fill in every square.
    If a move is invalid, the square will turn bright red.
    '''


    def __init__(self, board, solver):
        self.board = board
        self.solver = solver



    def on_clear_click(self):
        '''
        On-click listener for clearing the board
        Args:
            None
        Returns:
            None
        '''
        for index in self.string_vars.keys():
            self.string_vars[index].set("")
            self.board.set_cell(int(index), "*")



    def on_solve_click(self):
        '''
        On-click listener for solving the board
        Args:
            None
        Returns:
            None
        '''

        #Clear then solve
        for index in self.string_vars.keys():
            self.string_vars[index].set("")
            self.board.set_cell(int(index), "*")

        self.solver.solve()
        for i in range(81):
            if str(i) in self.string_vars.keys():
                cell = self.board.cells[i]
                self.string_vars[str(i)].set(str(cell))



    def on_help_click(self):
        '''
        On-click listener for help button
        Args:
            None
        Returns:
            None
        '''

        toplevel = tk.Toplevel()
        lbl_how_to = tk.Label(
            master=toplevel,
            text=self.help_str,
            font=("Courier", 16),
            height=0,
            width=80,
        )
        lbl_how_to.grid(row=0, column=0, padx=10, pady=10)



    def on_cell_changed(self, cell, index, value):
        '''
        On-change listener for a cell
        Args:
            cell - Cell Tkinter widget
            index - Index of the cell on the board
            value - Tkinter VarString of the value
        Returns:
            None
        '''

        cell.config(bg=self.BASE)
        if len(value.get()) == 0:
            return

        if len(value.get()) > 1:
            value.set(value.get()[:1])


        possible = "123456789"
        if not value.get()[0] in possible:
            value.set("")
            self.board.set_cell(index, "*")
            return

        num = int(value.get())
        try:
            self.board.play_move(index, num)
        except:
            cell.config(bg=self.WRONG_MOVE)
            


    def start(self):
        '''
        Starts the GUI instance
        Args:
            None
        Returns:
            None
        '''

        window = tk.Tk()
        window.title("SlickSudoku")

        top_buttons = tk.Frame(
            master=window,
            relief=tk.FLAT,
            borderwidth=1,
        )

        clear = tk.Button(
            master=top_buttons,
            text="Clear",
            font=("Courier", 22),
            bg=self.BASE,
            padx=10,
            pady=10,
            command=self.on_clear_click
        )
        clear.grid(row=0, column=0)

        solve = tk.Button(
            master=top_buttons,
            text="Solve",
            font=("Courier", 22),
            bg=self.BASE,
            padx=10,
            pady=10,
            command=self.on_solve_click
        )
        solve.grid(row=0, column=1)

        help_button = tk.Button(
            master=top_buttons,
            text="Help",
            font=("Courier", 22),
            bg=self.BASE,
            command=self.on_help_click,
            padx=10,
            pady=10
        )
        help_button.grid(row=0, column=2)

        top_buttons.grid(padx=5)

        board_frame = tk.Frame(
            master=window,
            relief=tk.FLAT,
            borderwidth=1,
        )
        board_frame.grid()

        for section_row in range(3):
            for section_col in range(3):
                section = tk.Frame(
                    master=board_frame,
                    relief=tk.GROOVE,
                    borderwidth=4,
                    padx=1,
                    pady=1
                )
                section.grid(row=section_row, column=section_col, sticky="nsew")


                for cell_row in range(3):
                    for cell_col in range(3):
                        row = section_row * 3 + cell_row
                        col = section_col * 3 + cell_col
                        index = row * 9 + col

                        cell = tk.Frame(
                            master=section,
                            relief=tk.FLAT,
                            borderwidth=1,
                            padx=1,
                            pady=1,
                        )
                        cell.grid(row=cell_row, column=cell_col, sticky="nsew")

                        value = self.board.get_cell(index)
                        if value != "*":
                            value_label = tk.Label(
                                master=cell,
                                bg=self.STATIC_INDICES,
                                text=f'{value}',
                                font=("Courier", 44),
                                width=2,
                            )
                            value_label.pack(fill="both", expand=True)

                        else:
                            sv = tk.StringVar()
                            value_label = tk.Entry(
                                master=cell,
                                bg=self.BASE, 
                                font=("Courier", 44),
                                width=2,
                                justify=tk.CENTER,
                                textvariable=sv
                            )
                            sv.trace("w", lambda name, index, mode, cell=value_label, sv=sv, 
                                index2=index: self.on_cell_changed(cell, index2, sv))
                            self.string_vars[str(index)] = sv
                            value_label.pack(fill="both", expand=True)


        window.mainloop()