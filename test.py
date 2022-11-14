"""
Test functions for wordle bot
"""

from tools import is_valid
import random
import statistics

words = []
with open("words.txt") as f:
    words = [word.strip() for word in f]

from game import Game

scores = []
wins = 0
losses = 0
for x in range(100):
    game = Game()
    valid_words = words
    score = 0
    for y in range(6):
        score += 1
        result = game.make_guess(random.choice(valid_words))
        valid_words = [word for word in valid_words if is_valid(game.history, word)]
        if result == "You Won!":
            wins += 1
            break
        if result == "You Lost!":
            losses += 1
            break
    print(score)
    scores.append(score)
print(scores)
print(statistics.mean(scores))
print("Wins: ", wins)
print("Losses: ", losses)