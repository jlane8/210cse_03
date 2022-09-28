"""
File: parachute.py
Author: Jerry Lane
Purpose: This class represents the parachute and what can happen
to it over time with wrong choices.
"""
# import Terminal class to instantiate a Terminal to use for player
# interactions
from game.terminal import Terminal

# class declaration
class Parachute:
    """
    Parameters: none
    Return: nothing
    This class represents the parachute object and handles the activities
    and results of band choices.
    """

    # constructor method
    def __init__(self):
        """
        Parameters: none
        Return: nothing
        This method will instantiate a Terminal, and create a fully formed
        parachute.
        """

        # create Terminal instance and create new jumper and chute
        self._terminal = Terminal()
        self.restore()
    
    # method to display the current jumper and parachute
    def display(self):
        """
        Parameters: none
        Return: nothing
        display sends the jumper list (parachute graphic) to the terminal 
        instance for printing to the console
        """
        
        # send current parachute list to console via Terminal
        self._terminal.display(self._jumper)

    # method to determine if the chute is functioning
    def has_chute(self):
        """
        Parameters: none
        Return: boolean
        If the parachute has degraded to where it is just the jumper and no chute,
        send back False, if the length of the jumper list has chute, return True
        """
        
        # if jumper list is at least 5 or more, return True unless it has a 'dead head'
        if len(self._jumper) >= 5 and self._jumper[0] != f"\033[1;31m      x      \033[00m":
            return True

        # otherwise return False    
        else:
            return False

    # method to reset jumper and parachute to new
    def restore(self):
        """
        Parameters: none
        Return: nothing
        This method merely creates the list for a fully formed jumper and parachute,
        as well as the dead jumper string used in the _has_chute method
        """
        
        # create good head for the jumper
        head = f"\033[00m\033[1;39m{chr(2)}\033[00m\033[1;37m"
        
        # create dead head for the jumper
        self._dead_jumper = f"\033[1;31m      x      \033[00m"
        
        # create list holding the strings which draw a jumper with parachute
        self._jumper = [
            "\033[1;33m     ___     \033[00m", "\033[1;33m   /_____\   \033[00m",
            "\033[1;37m   \     /   \033[00m", "\033[1;37m    \   /    \033[00m",
           f"\033[1;37m     \{head}/     \033[00m", 
            "\033[1;34m     /|\     \033[00m", "\033[1;34m     / \     \033[00m", "             ",
            "             ",                   "\033[1;30m   ^^^^^^^   \033[00m"]

    # method to check to see if there is any chute left
    def check_chute(self, guess):
        """
        Parameters: guess - a boolean sent by the Jumper class if a guess was wrong.
        Return: nothing
        If the guess was wrong (False) and the length of the jumper string is not five
        then the first element in the jumper list is deleted. This allows the has_chute
        method time to display the dead jumper's head if it reaches that point while
        gradually removing part of the chute with each bad guess.
        """
        
        # if guess is False and the length of the jumper list is not equal to five, 
        # delete the first element in the jumper list; if length is five, check to see
        # if self._jumper[0] is equal to the dead head string; if it is not, then
        # make self._jumper[0] equal to the dead head string, and afterward it will resume
        # the countdown.
        if not guess:
            if len(self._jumper) == 6 and self._jumper[0] != f"\033[1;31m      x      \033[00m":
                self._jumper[0] = f"\033[1;31m      x      \033[00m"
            else:
                del self._jumper[0]