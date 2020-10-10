# CS76 Problem Assignment 2 10/1/2020
# Authors: Sudharsan Balasubramani & Alberto
# Collaborators: Discussed strategies with James Fleming, Mack Reiferson

# import statements
import chess
from RandomAI import RandomAI
from HumanPlayer import HumanPlayer
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
from ChessGame import ChessGame
import sys

# For testing, create two players. In this case Human and Random. Have a game with them and run until it is over.

player1 = MinimaxAI(2, True)
player2 = RandomAI()
# player2 = MinimaxAI(3)

game = ChessGame(player1, player2)
# game.board.clear()
# game.board.set_epd("7k/8/8/8/8/8/8/RR6 w - -")
# game.board.set_piece_at(0, chess.Piece(4, chess.WHITE))
# game.board.set_piece_at(1, chess.Piece(4, chess.WHITE))
# game.board.set_piece_at(63, chess.Piece(6, chess.BLACK))
# print(game.board.epd())
while not game.is_game_over():
    print(game)
    game.make_move()

# print(hash(str(game.board)))
