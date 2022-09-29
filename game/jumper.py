"""
File: jumper.py
Author: Jerry Lane
Purpose: This class represents a jumper. It controls the game play
         using instantiations of the Parachute, Puzzle, and Terminal
         classes and internal methods of this class.
"""
# import the Parachute, Puzzle and Terminal classes
from game.parachute import Parachute
from game.puzzle    import Puzzle
from game.terminal  import Terminal

# class declaration
class Jumper:
    """
    Parameters: none
    Return: nothing
    This class handles all the actions of the game. Just as a jumper
    would take action to solve the problems of crashing from a 
    foiled parachute, so will the player through this class.
    """

    # default constructor
    def __init__(self):
        """
        Parameters: none
        Return: nothing
        This is the constructor method for the Jumper class
        """
        self._terminal = Terminal()
        self._parachute = Parachute(self._terminal)
        self._puzzle = Puzzle(self._terminal)
        self._health = self._has_health()
        self._is_playing = True
        self._letter_guessed = ""
        self._puzzle_solved = False
        self._has_won = False

    # method starting and controlling game
    def start_game(self):
        """
        Parameters: none
        Return: nothing
        This is the start game method, where all the game directives are
        handled.
        """
        while self._is_playing:            
            self._puzzle.show()
            self._parachute.display()
            self._letter_guessed = self._get_letter()
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

    def _get_letter(self):
        letter = ""
        validation_in_progress = True
        while validation_in_progress:
            letter = self._terminal.collect("Guess a letter: ")
            if len(letter) == 1 and letter.isalpha():
                validation_in_progress = False
            else:
                self._terminal.onscreen("Bad input. Only a single letter is accepted.")
                self._terminal.onscreen("Please try again.")
        return letter
    
    # check to see if there is any chute left, if you, 
    def _has_health(self):
        """
        Parameters: none
        Return: boolean sent from the Parachute class. 
        If the player has chute left, then they have life. If the chute is
        gone, so is the jumper's life.
        """
        return self._parachute.has_chute()

    # method of steps to take once the game has ended
    def _end_game(self):
        """
        Parameters: none
        Return: nothing
        This method handles the end game actions. It will reveal the puzzle through 
        the puzzle class. If the player won, it will display a congratulations message.
        Either way, it informs the player the game is over. Then, in the validate loop,
        the player indicates whether they will play again or not. If yes, the game is
        reset through the other classes, and if no, it gives a goodbye message and ends.
        Finally, the loop ensures that only "y" and "n" inputs from the player are 
        accepted.
        """
        # show puzzle and parachute end game state
        self._puzzle.show()
        self._parachute.display()

        # reveal the puzzle's secret word
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
                self._terminal.onscreen("Incorrect response, only 'y' and 'n' are accepted.")
                self._terminal.onscreen("Please try again.")