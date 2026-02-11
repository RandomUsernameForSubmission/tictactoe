import tkinter
from tkinter import messagebox


class GameView:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("TicTacToe")
        self.buttons = []

    def build_board(self, board_size, on_click):
        for column in range(board_size):
            buttons_in_cols = []
            for row in range(board_size):
                button = tkinter.Button(
                    self.window,
                    width=4,
                    height=4,
                    command=lambda x=row, y=column: on_click(x, y)
                )
                button.grid(column=column, row=row)
                buttons_in_cols.append(button)
            self.buttons.append(buttons_in_cols)

    def set_cell(self, x, y, pawn):
        self.buttons[y][x].config(text=pawn)

    def disable_all(self):
        for row in self.buttons:
            for button in row:
                button.config(state='disabled')
                
    def show_message(self, titre, message):
        return messagebox.showinfo(titre, message)

    def refresh(self):
        self.window.update_idletasks()

    def display_window(self):
        return self.window.mainloop()
    
    def reset_view(self):
        for column in self.buttons:
            for button in column:
                button['text'] = ''
                button['state'] = 'normal'
