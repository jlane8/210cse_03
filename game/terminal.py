class Terminal:

    def __init__(self):
        pass


    def display(self, jumper):
        print()
        for i in range(len(jumper)):
            print(jumper[i])
        print()


    def show(self, puzzle):
        print()
        for i in range(len(puzzle)):
            print("  " + puzzle[i], end = "")
        print()

    # method to display text onscreen
    def onscreen(self, prompt):
        print(prompt)
    
    # method to get input from player
    def collect(self, prompt):
        return input(prompt).lower()

    
    # method to have jumper fall and impact into the ground
    def splat(self, jumper):
        pass