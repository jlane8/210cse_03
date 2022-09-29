"""
File: terminal.py
Author: Jerry Lane
Purpose: This represents the Terminal class. It is the 
         input/output interface to the player.
"""

# class declaration
class Terminal:
    """
    Parameters: none
    Return: nothing
    This represents the keyboard and console display serving
    to interface with the player. Its methods handle all the
    various display options to show the player the puzzle, jumper,
    text, etc. It also gets any input from the player.
    """
    
    # constructor method
    def __init__(self):
        """
        Parameters: none
        Return: nothing
        This is a default constructor. It does nothing except be a 
        basic constructor.
        """
        
        # do nothing
        pass

    # method to display the jumper list to the player
    def display(self, jumper):
        """
        Parameter: the jumper list, sent by the Jumper class
        Return: nothing
        This method will take the jumper list from the Jumper class,
        and display it to the player in whatever form it currently 
        holds. 
        """
        
        # display clean line to separate the jumper from other text
        print()

        # line by line, display each string in the jumper list
        for i in range(len(jumper)):
            print(jumper[i])
        
        # display another clean line to separate the jumper
        print()

    # method to show the puzzle sent by the Puzzle class
    def show(self, puzzle):
        """
        Parameters: puzzle - sent by the Puzzle class
        Return: nothing
        This method will accept the puzzle list from the Puzzle class
        and display it to the player, one letter at a time. If any
        letters have been guessed by the player, they will be in
        the puzzle list that the Puzzle class amended before sending.
        """

        # clear the screen
        for i in range(40):
            print()

        # letter by letter, show the puzzle parameter to the player
        for i in range(len(puzzle)):
            print("  " + puzzle[i], end = "") # don't print new line
        
        # now print a new line
        print()

    # method to display text onscreen
    def onscreen(self, prompt):
        """
        Parameters: prompt - text sent by another class to be displayed
        Return: nothing
        This method accepts a prompt from one of the other classes and
        displays the prompt to the player.
        """
        
        # display what the other class wanted displayed
        print(prompt)
    
    # method to get input from player
    def collect(self, prompt):
        """
        Parameters: prompt - text to display when getting input from player
        Return: player's input
        This method accepts a prompt from the Jumper class, prints the message
        to the player, then returns the player's input back to the calling
        class.
        """
        
        # return player input in lower case form
        return input(prompt).lower()