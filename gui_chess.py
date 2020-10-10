# CS76 Problem Assignment 2 10/1/2020
# Authors: Sudharsan Balasubramani & Alberto
# Collaborators: Discussed strategies with James Fleming, Mack Reiferson

# import statements
from PyQt5 import QtGui, QtSvg
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import QApplication, QWidget
import sys
import chess, chess.svg
from RandomAI import RandomAI
from MinimaxAI import MinimaxAI
from ChessGame import ChessGame
from HumanPlayer import HumanPlayer

import random


# A GUI version of the Chess game that will be played by the AIs. Does not have to be used for this lab, but if have
# time take a looksie
class ChessGui:

    # Constructor for a Chess GUI, has a couple players, that will use the ChessGame class to store the game and then
    # use GUI elements to show a graphical rendition of the Chess game
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        self.game = ChessGame(player1, player2)

        self.app = QApplication(sys.argv)
        self.svgWidget = QtSvg.QSvgWidget()
        self.svgWidget.setGeometry(50, 50, 400, 400)
        self.svgWidget.show()

    # Starts the GUI
    def start(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.make_move)
        self.timer.start(10)

        self.display_board()

    # Display GUI board with svgs
    def display_board(self):
        svgboard = chess.svg.board(self.game.board)

        svgbytes = QByteArray()
        svgbytes.append(svgboard)
        self.svgWidget.load(svgbytes)

    # Has the chess game make a move, which has one of the players make a move.
    def make_move(self):

        print("making move, white turn " + str(self.game.board.turn))

        self.game.make_move()
        self.display_board()


if __name__ == "__main__":

    random.seed(1)

    #player_ronda = RandomAI()

    # to do: gui does not work well with HumanPlayer, due to input() use on stdin conflict
    #   with event loop.

    player1 = RandomAI()
    player2 = RandomAI()

    game = ChessGame(player1, player2)
    gui = ChessGui(player1, player2)

    gui.start()

    sys.exit(gui.app.exec_())
