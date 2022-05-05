# This program plays a game of Rock, Paper, Scissors between two Players,
# and reports both Player's scores each round.

# The Player class is the parent class for all of the Players
# in this game.


import random

# available moves to use for game
moves = ['rock', 'paper', 'scissors']


# Dwayne Johnson (computer player)
class Player:
    wins = 0
    my_move = ''
    their_move = ''

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


# Rando Calrissian (computer player)
class RandomPlayer(Player):
    def move(self):
        # sends move for round to Game class (play_round)
        return random_move()


# You (human player)
class HumanPlayer(Player):
    def move(self):
        while True:
            # gets player's move
            move = input().lower()

            # checks for valid input
            if move not in moves:
                print("Please type in a valid move.")
            else:
                break

        # sends move for round to Game class (play_round)
        return move


# The Reflector (computer player)
class ReflectPlayer(Player):
    def move(self):
        if self.their_move == '':
            # sends move for round to Game class (play_round)
            return random_move()
        else:
            # sends move for round to Game class (play_round)
            return self.their_move


# The Recycler (computer player)
class CyclePlayer(Player):
    def move(self):
        if self.my_move == '':
            # sends move for round to Game class (play_round)
            return random_move()
        else:
            # finds index of next move in list
            move = (moves.index(self.my_move) + 1) % len(moves)

            # sends move for round to Game class (play_round)
            return moves[move]


# chooses and returns random selection from moves list
def random_move():
    return random.choice(moves)


# determines winner of individual rounds
def round_winner(self, move1, move2):
    if move1 == move2:
        print("Tie!")
    else:
        if beats(move1, move2):
            print("Player One wins!")
            self.p1.wins += 1
        else:
            print("Player Two wins!")
            self.p2.wins += 1


# determines winning conditions
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


# game initializer
class Game:
    # player assignment
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    # plays out individual rounds of game
    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")

        # sends moves to determine winner
        round_winner(self, move1, move2)

        # displays current score
        print(f"\nPlayer One: {self.p1.wins} wins.\n"
              f"Player Two: {self.p2.wins} wins.\n")

        # allows each player to learn from past moves, if applicable
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    # main game structure
    def play_game(self):
        print("\nGame start!\n")

        # determines game length (by number of rounds)
        self.rounds = 5
        for round in range(self.rounds):
            print(f"Round {round + 1}:")
            self.play_round()

        # concludes game
        print("Game over!\n")
        print(f"With Player One having {self.p1.wins} wins and Player Two "
              f"having {self.p2.wins} wins...")

        # endings
        if self.p1.wins > self.p2.wins:
            # player one wins
            print("Player One claims victory!")
        elif self.p1.wins < self.p2.wins:
            # player two wins
            print("Player Two claims victory!")
        else:
            # tied game
            print("The game ends in a draw!")

        # exits program on input
        input()
        exit()


# picks and returns random opponent for game
def determine_opponent():
    opponents = (Player(), RandomPlayer(), ReflectPlayer(), CyclePlayer())
    return random.choice(opponents)


# entry point
if __name__ == '__main__':
    game = Game(HumanPlayer(), determine_opponent())
    game.play_game()
