from tkinter import simpledialog

from game_board import GameBoard
from game_state import GameState
from game_view import GameView

def ask_pawn():
    pawn = simpledialog.askstring("Choix du pion", "Choisissez votre pion (X ou O):")
    return pawn if pawn in ['X', 'O'] else 'X'

class TicTacToeApp:
    def __init__(self):
        self.player_pawn = ask_pawn()

        self.view = GameView()
        self.state = GameState(self.player_pawn)
        self.board = GameBoard(self.state, self.view, ask_pawn)

    def run(self):
        return self.view.display_window()

if __name__ == "__main__":
    app = TicTacToeApp()
    app.run()
