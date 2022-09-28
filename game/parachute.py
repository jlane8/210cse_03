from game.terminal import Terminal

class Parachute:

    def __init__(self):
        self.terminal = Terminal()
        self.restore()
    
    def display(self):
        """
        parameters: none
        return: nothing
        display sends the jumper list to the terminal object for
        printing to the console
        """
        self.terminal.display(self._jumper)


    def has_chute(self):
        if len(self._jumper) >= 5:
            return True
        else:
            self._jumper[0] = self._dead_jumper
            return False

    def restore(self):
        head = f"\033[00m\033[1;39m{chr(2)}\033[00m\033[1;37m"
        self._dead_jumper = f"\033[1;31m      x      \033[00m"
        self._jumper = [
            "\033[1;33m     ___     \033[00m", "\033[1;33m   /_____\   \033[00m",
            "\033[1;37m   \     /   \033[00m", "\033[1;37m    \   /    \033[00m",
           f"\033[1;37m     \{head}/     \033[00m", 
            "\033[1;34m     /|\     \033[00m", "\033[1;34m     / \     \033[00m", "             ",
            "             ",                   "\033[1;30m   ^^^^^^^   \033[00m"]

    def check_chute(self, guess):
        if not guess and len(self._jumper) != 5:
            del self._jumper[0]