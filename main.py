from game_controller import GameController
from game_state import GameState
from game_view import GameView


class TicTacToeApp:
    def __init__(self):
        self.view = GameView()
        self.state = GameState(self.view.ask_pawn())
        self.board = GameController(self.state, self.view)

    def run(self):
        return self.view.display_window()

if __name__ == "__main__":
    app = TicTacToeApp()
    app.run()
