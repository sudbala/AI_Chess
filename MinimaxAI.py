# CS76 Problem Assignment 2 10/1/2020
# Authors: Sudharsan Balasubramani & Alberto
# Collaborators: Discussed strategies with James Fleming, Mack Reiferson

# import statements
import chess
import random


# A Class to hold the Minimax AI that handles the minimax algorithm.
class MinimaxAI:

    # Constructor for the minimax algo
    def __init__(self, depth, ids=False):
        self.depth = depth
        self.material_dictionary = {1: 1, 2: 3, 3: 3, 4: 5, 5: 9}
        self.material_num = {1: 8, 2: 2, 3: 2, 4: 2, 5: 1}
        self.calls = 0
        self.ids = ids
        pass

    # Generates the minimax moves, chooses the move based on that search tree.
    def choose_move(self, board):
        # Set a depth starting at 0
        depth = 0
        move = self.minimax_decision(board, depth)
        if self.ids:
            print("Minimax IDS AI recommending move " + str(move) + " done in " + str(self.calls) + " minimax calls")
        else:
            print("Minimax AI recommending move " + str(move) + " done in " + str(self.calls) + " minimax calls")
        self.calls = 0
        return move

    # Grabs the decision for minimax. TODO: Change to just comparisons rather than dictionary
    def minimax_decision(self, board, depth):
        # Get a list of all the possible actions or moves. Declare a dictionary to get the move later on.
        moves = list(board.legal_moves)
        scores = {}
        # For each action, calculate the min-value. Then we take a max of it all
        max_move = None
        max_move_val = float('-inf')
        for move in moves:
            # give a move its min-value
            board.push(move)
            if self.ids:
                next_board_val = self.ids_search(board)
            else:
                next_board_val = self.min_value(board, depth + 1)
            if max_move_val < next_board_val:
                max_move_val = next_board_val
                max_move = move

            board.pop()

        print("Minimax Eval: " + str(max_move_val))

        # Now we need to find the best move based on the max of all the values associated with the moves
        return max_move

    # Should be returning a evaluation value
    def max_value(self, board, depth):
        # Document number of times we are entering minimax
        self.calls += 1
        # If we are at a cutoff state, then we should just return the evaluation function at that point
        if self.cutoff_test(board, depth):
            return self.evaluation_function(board, depth)
        # Otherwise, we keep going to find the max evaluation value for this given state. First we set our value to a
        # very high value. Then we grab the "actions" from this state, or just the list of legal moves
        val = float('-inf')
        moves = list(board.legal_moves)
        # Now loop over those actions, and find the max of that value and the Min-Value
        for move in moves:
            # Push that move, find the max
            board.push(move)
            val = max(val, self.min_value(board, depth + 1))
            # Make sure we pop that move to return back to the move from earlier
            board.pop()
        # Return val!
        return val

    # Should be returning the minimum of the evaluation function for a given part of the tree
    def min_value(self, board, depth):
        # Document number of times we are entering minimax
        self.calls += 1
        # If we are at a cutoff state, then we should just return the evaluation function at that point
        if self.cutoff_test(board, depth):
            return self.evaluation_function(board, depth)
        # Otherwise, we keep going to find the min evaluation value for this given state. First we set our value to a
        # very high value and then grab actions from this state, ie the legal moves.
        val = float('inf')  # High value :o
        moves = list(board.legal_moves)
        # Now loop over those moves, find the min of that value and the max_value
        for move in moves:
            # Push that move, find the min
            board.push(move)
            val = min(val, self.max_value(board, depth + 1))
            # Make sure we pop that move to return back to the chess board from earlier yuh
            board.pop()
        # Return val
        return val

    # Iterative Deepening component for the Minimax algorithm
    def ids_search(self, board):
        # Do for a depth within the max depth limit
        best_value = 0
        for depth in range(self.depth):
            # Call the min function from minimax
            value = self.min_value(board, self.depth - depth)
            # Make sure to replace best_value if value is the better
            if value > best_value:
                best_value = value
        # return the best of the values yuh
        return best_value

    def evaluation_function(self, board, depth):
        # Grab the turn
        turn = board.turn

        # Set val equal to 0, then calculate the eval function
        val = 0
        for i in range(1, 6):
            if turn == chess.WHITE:
                val += self.material_dictionary[i]*len(board.pieces(i, chess.WHITE))
                val += self.material_dictionary[i]*(self.material_num[i] - len(board.pieces(i, chess.BLACK)))
            elif turn == chess.BLACK:
                val += self.material_dictionary[i]*len(board.pieces(i, chess.BLACK))
                val += self.material_dictionary[i] * (self.material_num[i] - len(board.pieces(i, chess.WHITE)))
        if turn == chess.WHITE:
            val += 1 - len(board.pieces(6, chess.BLACK))
        else:
            val += 1 - len(board.pieces(6, chess.WHITE))

        if len(list(board.legal_moves)) <= 8:
            val += 20 * (8 - len(list(board.legal_moves)))

        if board.is_checkmate():
            val += 50*(self.depth - depth)
        return val


    def cutoff_test(self, board, depth):
        return board.is_game_over() or depth > self.depth
