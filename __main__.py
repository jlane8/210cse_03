"""
File: __main__.py
Author: Jerry Lane
Purpose:
    The __main__.py file will launch the Jumper game by creating a Jumper
    instantiation and calling the start_game method on it.
"""
from game.jumper import Jumper

jumper = Jumper()
jumper.start_game()