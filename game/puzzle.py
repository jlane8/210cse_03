import random
from game.terminal import Terminal

class Puzzle:

    def __init__(self):
        self._words = ["class", "object", "programming", "course",\
                       "parachute", "emergency", "skydiving", "thrill",\
                       "danger", "falling", "solve", "survive", "wait"]
        self._secret = self._words[random.randint(0, len(self._words) - 1)]
        self._terminal = Terminal()
        self._make_puzzle()

    def show(self):
        self._terminal.show(self._puzzle)

    def check_guess(self, guess):
        if guess in self._secret:
            self._amend_puzzle(guess)
            return True
        else:
            return False

    def _make_puzzle(self):
        self._puzzle = []
        for i in range(len(self._secret)):    
            self._puzzle.append("_")

    def _amend_puzzle(self, guess):
        for i in range(len(self._secret)):
            if self._secret[i] == guess:
                self._puzzle[i] = guess

    def has_won(self):
        for i in range(len(self._puzzle)):
            if self._puzzle[i] == "_":
                return False
        return True

    def reveal(self):
        self._terminal.onscreen(f"The secret word was: {self._secret}")

    
    def new_puzzle(self):
        temp = self._secret
        no_duplicates = True
        while no_duplicates:
            self._secret = self._words[random.randint(0, len(self._words) - 1)]
            if self._secret != temp:
                no_duplicates = False
        self._make_puzzle()