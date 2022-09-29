"""
File: puzzle.py
Author: Jerry Lane
Purpose: This class represents the word puzzle and actions dealing with
the puzzle.
"""

# import the random module
import random

# class declaration
class Puzzle:
    """
    Parameters: terminal - shares same terminal instatiation with caller
    Return: nothing
    This class represents the secret word to be guessed, and all the actions
    involving it such as hiding the secret word in a underlined puzzle which
    the player must guess the letters of.
    """
    
    # constructor method
    def __init__(self, terminal):
        """
        Parameters: terminal - shares same terminal instatiation with caller
        Return: nothing
        This constructor method creates a secret word list from which the secret
        word is selected at random. A Terminal instance is created, so this class
        can interact with the player through the console. Lastly, it calls the
        method to create the new puzzle the player must solve to save the jumper.
        """
        
        # create list of secret words
        self._words = ["class", "object", "programming", "course",\
                       "parachute", "emergency", "skydiving", "thrill",\
                       "danger", "falling", "solve", "survive", "wait"]
        
        # select the secret word for this puzzle from the _words list
        self._secret = self._words[random.randint(0, len(self._words) - 1)]
        
        # create a Terminal instance
        self._terminal = terminal

        # create the new puzzle
        self._make_puzzle()

    # method to send the puzzle to the Terminal for display
    def show(self):
        """
        Parameters: none
        Return: nothing
        This method just sends the current puzzle to the Terminal for the
        player to view its status.
        """

        # send the puzzle in its current state to the Terminal for viewing
        self._terminal.show(self._puzzle)

    # method to check player's guess
    def check_guess(self, guess):
        """
        Parameters: none
        Return: boolean signifying whether the player's guessed letter is in
        the puzzle.
        If the letter is there, the puzzle is amended, to show where the 
        letter(s) is/are and returns True. If not, it simply returns False.
        """
        
        # if the guessed letter is in the secret word, amend the puzzle string
        # to reflect that and return True; if it is not, return False
        if guess in self._secret:
            self._amend_puzzle(guess)
            return True
        else:
            return False

    # method to make a new puzzle from the secret word
    def _make_puzzle(self):
        """
        Parameters: none
        Return: nothing
        This method will empty the puzzle list, which holds the puzzle letters itself.
        In order to create a new puzzle, for each of the letters in the secret word,
        the method puts an underscore. This hides the secret word from the player,
        require them to guess at the letters in it.
        """

        # empty any previous puzzle elements
        self._puzzle = []

        # loop through the length of the secret word, to ensure the underscores match
        # the number of letters in the secret word, and append the underscore to the
        # new puzzle
        for i in range(len(self._secret)):    
            self._puzzle.append("_")

    # method to show letters when a player guesses correctly
    def _amend_puzzle(self, guess):
        """
        Parameters: guess - a letter the player has guessed to be in the secret word
        Return: nothing
        This method takes the player's guessed letter and amends the puzzle list to 
        reflect where the letter is in the puzzle
        """

        # loop through the length of the secret word, if the guessed letter matches,
        # change the puzzle element to the guessed letter, otherwise, leave it alone.
        for i in range(len(self._secret)):
            if self._secret[i] == guess:
                self._puzzle[i] = guess

    # method to check to see if the player has solved for the secret word correctly
    def has_won(self):
        """
        Parameters: none
        Return: False if there are any underscore elements in the puzzle list, else True
        This method checks to see if there are any unsolved letters in the puzzle. If there
        are, the method returns False, indicating the player has not won, and if there are
        none, the method returns True since it found no unsolved letters. 
        """

        # loop through the length of the puzzle
        for i in range(len(self._puzzle)):
            
            # if any unsolved letters exist, player has not won, return False
            if self._puzzle[i] == "_":
                return False
        
        # if there are no unsolved places, return True; player has won
        return True

    # method to reveal what the secret word was
    def reveal(self):
        """
        Parameters: none
        Return: none
        This method will access the Terminal's onscreen method, displaying a message
        telling the player what the secret word was.
        """

        # send message to the Terminal's onscreen method, including the secret word
        self._terminal.onscreen(f"The secret word was: {self._secret}")

    # method to creat a new puzzle if player decides to play again
    def new_puzzle(self):
        """
        Parameters: none
        Return: nothing
        This method remembers what the previous secret word was and enters a loop so the
        same word cannot be the new puzzle's secret word. While in the loop a new secret
        word is selected and compared to the old one, if it is the same, it loops again 
        for another chance to get a different secret word. Once the new, different, secret
        word is selected, it calls the _make puzzle method to create the new puzzle for it.
        """

        # remember the old secret word
        temp = self._secret

        # set the control loop variable to True
        no_duplicates = True

        # loop until there are no duplicates to the old secret word
        while no_duplicates:

            # select new secret word from the list of secret words
            self._secret = self._words[random.randint(0, len(self._words) - 1)]

            # if the selected word is different, turn off the loop
            if self._secret != temp:
                no_duplicates = False

        # now that we have a different secret word, make the new puzzle based on it        
        self._make_puzzle()