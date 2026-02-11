import pytest

from game_state import GameState


def test_move_places_pawn():
    state = GameState("X")
    assert state.move("X", 0, 0) is True
    assert state.board[0][0] == "X"


def test_move_rejects_occupied_cell():
    state = GameState("X")
    state.move("X", 1, 1)
    assert state.move("O", 1, 1) is False


def test_check_win_row():
    state = GameState("X")
    state.move("X", 0, 0)
    state.move("X", 1, 0)
    state.move("X", 2, 0)
    assert state.check_win("X") is True


def test_check_win_column():
    state = GameState("X")
    state.move("O", 1, 0)
    state.move("O", 1, 1)
    state.move("O", 1, 2)
    assert state.check_win("O") is True


def test_check_win_diagonal():
    state = GameState("X")
    state.move("X", 0, 0)
    state.move("X", 1, 1)
    state.move("X", 2, 2)
    assert state.check_win("X") is True


def test_is_draw():
    state = GameState("X")
    moves = [
        ("X", 0, 0), ("O", 1, 0), ("X", 2, 0),
        ("X", 0, 1), ("O", 1, 1), ("O", 2, 1),
        ("O", 0, 2), ("X", 1, 2), ("X", 2, 2),
    ]
    for pawn, x, y in moves:
        state.move(pawn, x, y)
    assert state.is_draw() is True


def test_reset_state():
    state = GameState("X")
    state.move("X", 0, 0)
    state.reset_state("O")
    assert state.player_pawn == "O"
    assert state.computer_pawn == "X"
    assert state.board[0][0] == ""
