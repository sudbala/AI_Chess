# CS76 Problem Assignment 2 10/5/2020
# Authors: Sudharsan Balasubramani & Alberto
# Collaborators: Discussed strategies with James Fleming, Mack Reiferson

import chess
import random
from time import sleep


class RandomAI:

    # Constructor for the random AI
    def __init__(self):
        pass

    # Provided a board, generate a list of legal moves and select a random one for the Random AI
    def choose_move(self, board):
        moves = list(board.legal_moves)
        move = random.choice(moves)
        sleep(1)  # I'm thinking so hard.
        print("Random AI recommending move " + str(move))
        return move
