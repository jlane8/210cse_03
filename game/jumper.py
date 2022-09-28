from game.parachute import Parachute
from game.puzzle    import Puzzle
from game.terminal  import Terminal

class Jumper:

    def __init__(self):
        """
        Parameters: none
        Return: nothing
        This is the constructor method for the Jumper class
        """
        self._parachute = Parachute()
        self._terminal = Terminal()
        self._puzzle = Puzzle()
        self._health = self._has_health()
        self._is_playing = True
        self._letter_guessed = ""
        self._puzzle_solved = False
        self._has_won = False

    # method starting and controlling game
    def start_game(self):
        while self._is_playing:            
            self._puzzle.show()
            self._parachute.display()
            self._letter_guessed = self._terminal.collect("Guess a letter: ")
            self._letter_is_good = self._puzzle.check_guess(self._letter_guessed)
            if not self._letter_is_good:
                self._parachute.check_chute(self._letter_is_good)
                if not self._has_health():
                    self._parachute.display()
                    self._end_game()
            else:
                if self._puzzle.has_won():
                    self._has_won = True
                    self._end_game()

    # check to see if there is any chute left, if you, 
    def _has_health(self):
        return self._parachute.has_chute()

    def _end_game(self):
        
        # reveal the puzzle
        self._puzzle.reveal()

        # if player won, give congrats
        if self._has_won:
            self._terminal.onscreen("Congratulations, you saved the jumper!")        
        
        # let player know the game is over in preparation for exit or new game
        self._terminal.onscreen("Game over!\n")
        
        # get valid input and either reset for new game or setup for exit
        validate = True
        while validate:    
            again = self._terminal.collect("Would you like to play again? y/n ")
            
            # if yes, reset the game so player can play again and end this loop
            if again == "y":
                self._has_won = False
                self._parachute.restore()
                self._puzzle.new_puzzle()
                validate = False
            
            # if no, give goodbye message, end game and this loop
            if again == "n":
                validate = False
                self._is_playing = False
                self._terminal.onscreen("Thanks for playing.\nGoodbye!\n")
            
            # if neither yes or no, let player know the input was wrong
            if again != "y" and again != "n":
                self._terminal.onscreen("Incorrect response, try again.")
