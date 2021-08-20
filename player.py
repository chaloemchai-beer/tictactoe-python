import math
import random

class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    # we want all player to get their next move given a game
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # get a random vaild spot for our next move
        square = random.choice(game.availble_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn, Input move (0-9):')
            # we're going to check that this is a correct value be trying to cast
            # it to an integer, and if it's not, then we say its invaild
            # if that spot is not availble on the board, we also say its invaild
            try:
                val = int(square)
                if val not in game.availble_moves():
                    raise ValueError
                vaild_square = True # if these are successful, then yay!
            except ValueError:
                print('Invaild square. Try again.')

        return val