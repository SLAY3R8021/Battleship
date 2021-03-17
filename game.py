#Creating an Intro and setting up the game
print("\n---LET'S PLAY BATTLESHIP---")
print("\nFirst let's create out battleships. Here is your grid.\n")

class Grid:
    def __init__(self, size):
        self.size = size
        self.grid = []
        
    def creating_grid(self):
        alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        num = []
        for i in range(self.size + 1):
            if i < 10:
                num.append("  {}   ".format(i))
            else:
                num.append("  {}  ".format(i))
        self.grid.append(num)
        for i in range(1, self.size + 1):
            temp = []
            for t in range(self.size + 1):
                if t == 0:
                    temp.append("  {}  /".format(alpha[i-1]))
                else:
                    temp.append("     /")
            self.grid.append(temp)
    
    def print_grid(self):
        for i in range(self.size + 1):
            temp = self.grid[i]
            string = ""
            for t in range(self.size + 1):
                val = temp[t]
                string += val
            print(string)

class Battleship:
    def __init__(self, size, location, direction):
        self.size = size
        self.location = location
        self.direction = direction

grid = Grid(10)
grid.creating_grid()
grid.print_grid()
