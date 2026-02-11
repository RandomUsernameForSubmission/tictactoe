import random

from game_state import GameState
from tkinter import messagebox

class GameBoard:
    def __init__(self, state: GameState, view):
        self.state = state
        self.view = view
        self.view.build_board(self.state.board_size, self.player_move)

    def player_move(self, x, y):
        if not self.state.move(self.state.player_pawn, x, y):
            return
        self.view.set_cell(x, y, self.state.player_pawn)
        if not self.game_check(self.state.player_pawn, "Vous avez gagné !"):
            self.computer_move()

    def computer_move(self):
        empty_cells = self.state.get_empty_cells()
        if not empty_cells:
            return
        x, y = random.choice(empty_cells)
        self.state.move(self.state.computer_pawn, x, y)
        self.view.set_cell(x, y, self.state.computer_pawn)
        self.game_check(self.state.computer_pawn, "L'ordinateur a gagné !")
            
    def game_check(self, pawn, victory_message):
        if self.state.check_win(pawn):
            self.view.refresh()
            self.view.show_message("Fin de partie", victory_message)
            self.view.disable_all()
            self.replay()
            return True
        elif self.state.is_draw():
            self.view.refresh()
            self.view.show_message("Fin de partie", "Match nul !")
            self.view.disable_all()
            self.replay()
            return True
        return False

    def replay(self):
        replay = messagebox.askyesno("Nouvelle partie", "Voulez-vous rejouer ?")
        if replay == True:
            new_player_pawn = self.view.ask_pawn()
            self.state.reset_state(new_player_pawn)
            self.view.reset_view()
        else:
            self.view.window.destroy()
