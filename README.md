# Jumper
If you love thrill and danger, you've come to the right place. Jumper is a game that will have you on the edge of your seat. Someone has jumped, and they are wearing a parachute. There's a problem, though; the cords are tangled and if you can't guess the secret word before the chute is fouled, the jumper falls to their demise. Can you solve the problem in time? The jumper's survival is up to you!

---
## Getting Started
Make sure you have Python 3.10.0 or newer installed and running on your machine. Open a terminal and browse to the project's root folder. Start the program by running the following command.
```
python3 __main__.py
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. Select the __main__ module inside the root folder and click the "run" icon.

## Project Structure
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- __main__.py         (program entry point)
  game                  (game folder)
  +-- puzzle            (word puzzle class)
  +-- chute             (parachute class)
  +-- terminal          (I/O class for input/display)
  +-- jumper            (jumper directs the action)
+-- README.md           (general info)
```

## Required Technologies
* Python 3.10.0

## Author
* Jerry Lane

## Game Rules
The puzzle is a secret word randomly chosen from a list.
The player guesses a letter in the puzzle.
If the guess is correct, the letter is revealed.
If the guess is incorrect, a line is cut on the player's parachute.
If the puzzle is solved the jumper is saved and the game is over.
If the player has no more parachute the jumper falls and the game is over.

