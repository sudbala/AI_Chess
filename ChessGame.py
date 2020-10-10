# CS76 Problem Assignment 2 10/1/2020
# Authors: Sudharsan Balasubramani & Alberto
# Collaborators: Discussed strategies with James Fleming, Mack Reiferson

import chess


# A class to hold a chess object and make process easier
class ChessGame:

    # Start with a player 1, player 2, and set the board based on chess.Board(), which gets a starting Board.
    # Also sets the list of two players
    def __init__(self, player1, player2):
        self.board = chess.Board()
        self.players = [player1, player2]

    # Based on turn, has corresponding player, which will be an AI or human, choose a move given a board and then push
    # that move to the actual board
    def make_move(self):

        player = self.players[1 - int(self.board.turn)]
        move = player.choose_move(self.board)

        self.board.push(move)  # Make the move

    # Checks if the game is over using the chess package's is_game_over() function.
    def is_game_over(self):
        return self.board.is_game_over()

    # String representation of the chess board, letting the outside know whose turn it is.
    def __str__(self):

        column_labels = "\n----------------\na b c d e f g h\n"
        board_str = str(self.board) + column_labels

        # did you know python had a ternary conditional operator?
        move_str = "White to move" if self.board.turn else "Black to move"

        return board_str + "\n" + move_str + "\n"
