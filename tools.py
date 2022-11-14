"""
Testing Wordle Python Methods
"""


class History:
    """
    Hint Data Class
    """
    def __init__(self, hints: dict):
        self.hints = hints
        self.grey_letters = set(
                [guess[x] for guess, hint in self.hints.items() \
                          for x in range(len(hint)) if hint[x] == 0]
                            )
        self.orange_letters = set(
                [guess[x] for guess, hint in self.hints.items() \
                          for x in range(len(hint)) if hint[x] == 1]
                              )
        self.green_letters = set(
                [(guess[x], x) for guess, hint in self.hints.items() \
                          for x in range(len(hint)) if hint[x] == 2]
                             )
    def __str__(self):
        return str(self.hints)


def is_valid(history: History, word: str) -> bool:
    """
    Return If Word is valid guess
    :param history:
    :param word:
    """
    # Check that word does not contain any grey letters
    for c in word:
        if c in history.grey_letters:
            return False
    # Check that all orange letters are present
    for c in history.orange_letters:
        if c not in word:
            return False
    # Check that all green letters are in their correct index
    for c, i in history.green_letters:
        if word[i] != c:
            return False
    # Check that no orange letter exists in an already guessed location
    for i, c in enumerate(word):
        if c in history.orange_letters and c not in [x[0] for x in history.green_letters]:
            for guess, hint in history.hints.items():
                if [True for x in range(len(guess)) if guess[x] == c and x == i]:
                    return False
    return True
    

def is_valid_debug(history: History, word: str) -> bool:
    """
    Return If Word is valid guess
    :param history:
    :param word:
    """
    # Check that word does not contain any grey letters
    for c in word:
        if c in history.grey_letters:
            print("fail check 1")
            return False
    # Check that all orange letters are present
    for c in history.orange_letters:
        if c not in word:
            print("fail check 2")
            return False
    # Check that all green letters are in their correct index
    for c, i in history.green_letters:
        if word[i] != c:
            print("fail check 3")
            return False
    # Check that no orange letter exists in an already guessed location
    for i, c in enumerate(word):
        if c in history.orange_letters and c not in [x[0] for x in history.green_letters]:
            for guess, hint in history.hints.items():
                if [True for x in range(len(guess)) if guess[x] == c and x == i]:
                    print("fail check 4")
                    print((i,c))
                    print((guess, hint))
                    return False
    return True
