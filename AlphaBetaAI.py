# CS76 Problem Assignment 2 10/1/2020
# Authors: Sudharsan Balasubramani & Alberto
# Collaborators: Discussed strategies with James Fleming, Mack Reiferson

import chess
from math import inf


# Will handle the alpha-beta pruning AI for AI based chess
class AlphaBetaAI:

    # Constructor for the minimax algo
    def __init__(self, depth):
        self.depth = depth
        self.material_dictionary = {1: 1, 2: 3, 3: 3, 4: 5, 5: 9}
        self.material_num = {1: 8, 2: 2, 3: 2, 4: 2, 5: 1}
        self.calls = 0
        pass

    # Generates the minimax moves, chooses the move based on that search tree.
    def choose_move(self, board):
        # Set a depth starting at 0
        depth = 0
        move = self.minimax_decision(board, depth)
        print("Alpha Beta AI recommending move " + str(move) + " done in " + str(self.calls) + " AlphaBeta calls")
        self.calls
        return move

    # Grabs the decision for minimax. TODO: Change to just comparisons rather than dictionary
    def minimax_decision(self, board, depth):
        # Get a list of all the possible actions or moves. Declare a dictionary to get the move later on.
        moves = self.reorder_moves(board, list(board.legal_moves))
        # moves = list(board.legal_moves)
        scores = {}
        # For each action, calculate the min-value. Then we take a max of it all
        max_move = None
        max_move_val = float('-inf')
        for move in moves:
            # give a move its min-value
            board.push(move)
            next_board_val = self.min_value(board, depth + 1, float('-inf'), float('inf'))
            if max_move_val < next_board_val:
                max_move_val = next_board_val
                max_move = move

            board.pop()

        print("AlphaBeta Eval: " + str(max_move_val))

        # Now we need to find the best move based on the max of all the values associated with the moves
        return max_move

    # Should be returning a evaluation value
    def max_value(self, board, depth, alpha, beta):
        # Increment number of calls
        self.calls += 1
        # If we are at a cutoff state, then we should just return the evaluation function at that point
        if self.cutoff_test(board, depth):
            return self.evaluation_function(board, depth)
        # Otherwise, we keep going to find the max evaluation value for this given state. First we set our value to a
        # very high value. Then we grab the "actions" from this state, or just the list of legal moves
        val = float('-inf')
        # moves = list(board.legal_moves)
        moves = self.reorder_moves(board, list(board.legal_moves))
        # Now loop over those actions, and find the max of that value and the Min-Value
        for move in moves:
            # Push that move, find the max
            board.push(move)
            val = max(val, self.min_value(board, depth + 1, alpha, beta))
            # Make sure we pop that move to return back to the move from earlier
            board.pop()
            # Update alpha and prune if possible!
            alpha = max(alpha, val)
            if beta <= alpha:
                break
        # Return val!
        return val

    # Should be returning the minimum of the evaluation function for a given part of the tree
    def min_value(self, board, depth, alpha, beta):
        # Increment number of calls
        self.calls += 1
        # If we are at a cutoff state, then we should just return the evaluation function at that point
        if self.cutoff_test(board, depth):
            return self.evaluation_function(board, depth)
        # Otherwise, we keep going to find the min evaluation value for this given state. First we set our value to a
        # very high value and then grab actions from this state, ie the legal moves.
        val = float('inf')  # High value :o
        # moves = list(board.legal_moves)
        moves = self.reorder_moves(board, list(board.legal_moves))
        # Now loop over those moves, find the min of that value and the max_value
        for move in moves:
            # Push that move, find the min
            board.push(move)
            val = min(val, self.max_value(board, depth + 1, alpha, beta))
            # Make sure we pop that move to return back to the chess board from earlier yuh
            board.pop()
            # Update beta and do pruning if possible
            beta = min(beta, val)
            if beta <= alpha:
                break
        # Return val
        return val

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
        # if board.turn == chess.BLACK:
        #     val = -val
        return val

    # Reorder moves in terms of whether the move is a capture or not
    def reorder_moves(self, board, moves):
        # New list of reordered moves
        reordered_moves = []
        # Now we iterate through old moves, check out which move is a capture, move it to front
        for move in moves:
            # check if capture, add to front if it is, back if not
            if board.is_capture(move):
                reordered_moves.insert(0, move)
            else:
                reordered_moves.append(move)
        return reordered_moves


    def cutoff_test(self, board, depth):
        return board.is_game_over() or depth > self.depth

