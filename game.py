"""
Wordle Game Simulator
"""
import random
from tools import History

words = []
with open("words.txt") as f:
    words = [word.strip() for word in f]


class Game:
    """
    Wordle Game Class
    """
    def __init__(self):
        self.word = random.choice(words)
        self.history = History({})
        self.score = 0
    
    def make_guess(self, guess):
        self.score += 1
        hint = {guess: [(0 if guess[i] not in self.word else (2 if guess[i] == self.word[i] else 1)) for i, c in enumerate(guess)]}
        # print(hint)
        self.history = History(self.history.hints | hint)
        # print(str(self.history))
        if hint[guess] == [2, 2, 2, 2, 2]:
            return self.end_game(True)
        if self.score > 5:
            return self.end_game(False)
        return "Guess again"

    def end_game(self, win: bool):
        if win:
            return "You Won!"
        else:
            return "You Lost!"