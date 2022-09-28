"""
File: __main__.py
Author: Jerry Lane
Purpose:
    The __main__.py file will launch the Jumper game by creating a Jumper
    instantiation and calling the start_game method on it.
"""
# import the Jumper class to instantiate the Jumper
from game.jumper import Jumper

# create Jumper instantiation, call the Jumper start_game method
jumper = Jumper()
jumper.start_game()