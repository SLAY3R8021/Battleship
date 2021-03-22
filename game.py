import sys

class Grid:
    def __init__(self, size, player):
        self.size = size
        self.player = player
        self.ship = []
        self.shot = []
        self.count = 0
        
    def create_grid(self):
        alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        num = []
        for i in range(self.size + 1):
            if i < 10:
                num.append("  {}   ".format(i))
            else:
                num.append("  {}  ".format(i))
        self.ship.append(num)
        for i in range(1, self.size + 1):
            temp = []
            for t in range(self.size + 1):
                if t == 0:
                    temp.append("  {}  |".format(alpha[i-1]))
                else:
                    temp.append("     |")
            self.ship.append(temp)
        num = []
        for i in range(self.size + 1):
            if i < 10:
                num.append("  {}   ".format(i))
            else:
                num.append("  {}  ".format(i))
        self.shot.append(num)
        for i in range(1, self.size + 1):
            temp = []
            for t in range(self.size + 1):
                if t == 0:
                    temp.append("  {}  |".format(alpha[i-1]))
                else:
                    temp.append("     |")
            self.shot.append(temp)
    
    def print_grid(self, choice):
        if choice == "ship":
            for i in range(self.size + 1):
                temp = self.ship[i]
                string = ""
                for t in range(self.size + 1):
                    val = temp[t]
                    string += val
                print(string)
        if choice == "shot":
            for i in range(self.size + 1):
                temp = self.shot[i]
                string = ""
                for t in range(self.size + 1):
                    val = temp[t]
                    string += val
                print(string)
    
    def create_ship(self, location, direction, ship_size):
        alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        for j in range(1, len(alpha) + 1):
            if str(location[0]) == str(alpha[j - 1]):
                col = int(location[1])
                pot = j
                row = self.ship[pot]
                move_count = 1
                pcol = col
                ppot = pot
                prow = row
                pmove_count = move_count
                if direction == "U" and (j - ship_size) < 0:
                    return print("\nInvalid placement. Try different spot.")
                elif direction == "R" and (int(location[1]) + ship_size - 1) > self.size:
                    return print("\nInvalid placement. Try different spot.")
                elif direction == "D" and (j + ship_size - 1) > self.size:
                    return print("\nInvalid placement. Try different spot.")
                elif direction == "L" and (int(location[1]) - ship_size) < 0:
                    return print("\nInvalid placement. Try different spot.")
                else:
                    if direction == "L":
                        while pmove_count <= ship_size:
                            if prow[pcol] == "     |":
                                pass
                            else:
                                return print("\nShips overlap. Please choose another spot or different direction.")
                            pcol -= 1
                            pmove_count += 1
                        row[col] = "  S  |"
                        self.count += ship_size
                        while move_count < ship_size:
                            col -= 1
                            row[col] = "  S  |"
                            move_count += 1
                        self.ship[pot] = row
                    elif direction == "R":
                        while pmove_count <= ship_size:
                            if prow[pcol] == "     |":
                                pass
                            else:
                                return print("\nShips overlap. Please choose another spot or different direction.")
                            pcol += 1
                            pmove_count += 1
                        row[col] = "  S  |"
                        self.count += ship_size
                        while move_count < ship_size:
                            col += 1
                            row[col] = "  S  |"
                            move_count += 1
                        self.ship[pot] = row
                    elif direction == "U":
                        while pmove_count <= ship_size:
                            if prow[pcol] == "     |":
                                pass
                            else:
                                return print("\nShips overlap. Please choose another spot or different direction.")
                            ppot -= 1
                            prow = self.ship[ppot]
                            pmove_count += 1
                        row[col] = "  S  |"
                        self.count += ship_size
                        self.ship[pot] = row
                        while move_count < ship_size:
                            pot -= 1
                            row = self.ship[pot]
                            row[col] = "  S  |"
                            self.ship[pot] = row
                            move_count += 1
                    elif direction == "D":
                        while pmove_count <= ship_size:
                            if prow[pcol] == "     |":
                                pass
                            else:
                                return print("\nShips overlap. Please choose another spot or different direction.")
                            ppot += 1
                            prow = self.ship[ppot]
                            pmove_count += 1
                        row[col] = "  S  |"
                        self.count += ship_size
                        self.ship[pot] = row
                        while move_count < ship_size:
                            pot += 1
                            row = self.ship[pot]
                            row[col] = "  S  |"
                            self.ship[pot] = row
                            move_count += 1
                    else:
                        return print("\nDirection or location is invalid. Please enter a new spot.")

    def check(self):
        num = self.count
        return num

    def shoot(self, location):
        alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        for j in range(1, len(alpha) + 1):
            if str(location[0]) == str(alpha[j - 1]):
                sp = self.ship[j]
                st = self.shot[j]
                col = int(location[1])
                if sp[col] == "  S  |":
                    st[col] = "  X  |"
                    self.count -= 1
                    self.shot[j] = st
                    print("\n---DIRECT HIT---")
                else:
                    st[col] = "  O  |"
                    self.shot[j] = st
                    print("\n---MISS---")
                if self.count == 0:
                    print("\n---{} WINS---".format(self.player))
                    sys.exit()

p1 = Grid(9, "PLAYER 1")
p2 = Grid(9, "PLAYER 2")
p1.create_grid()
p2.create_grid()
print("---LET'S PLAY BATTLESHIP---")
print("\nHere is the grid that you will be playing on.")
p1.print_grid("ship")
print("\nTime for Player 1 to create their ships")
print("\nYou'll create the ships by entering a location on the grid and a direction.")
print("\nMake sure Player 2 can't see your entries.")
p1s = 1
p1c = 0
while p1s <= 6:
    if p1s <= 3:
        ship_size = 3
    elif p1s <= 5:
        ship_size = 4
    else:
        ship_size = 5
    location = str(input("\nThis ships size will be {} units long.\nEnter your location.\n".format(ship_size)))
    direction = str(input("\nEnter your direction.\nU for up.\nD for down.\nL for left.\nR for right.\n"))
    p1.create_ship(location, direction, ship_size)
    p1a = p1.check()
    if p1a > p1c:
        p1c = p1a
        p1.print_grid("ship")
        p1s += 1
    else:
        pass
print("\n" * 1000)
print("\nNow it is Player 2 turn.")
p2.print_grid("ship")
p2s = 1
p2c = 0
while p2s <= 6:
    if p2s <= 3:
        ship_size = 3
    elif p2s <= 5:
        ship_size = 4
    else:
        ship_size = 5
    location = str(input("\nThis ships size will be {} units long.\nEnter your location.\n".format(ship_size)))
    direction = str(input("\nEnter your direction.\nU for up.\nD for down.\nL for left.\nR for right.\n"))
    p2.create_ship(location, direction, ship_size)
    p2a = p2.check()
    if p2a > p2c:
        p2c = p2a
        p2.print_grid("ship")
        p2s += 1
    else:
        pass
print("\n" * 1000)
print("\nNow it's time to start shooting.")
while True:
    for i in range(1000000):
        if (i % 2) == 0:
            print("\nPlayer 1's turn")
            p1.print_grid("shot")
            stock = str(input("\nEnter a location.\n"))
            p1.shoot(stock)
        else:
            print("\nPlayer 2's turn")
            p2.print_grid("shot")
            stock = str(input("\nEnter a location.\n"))
            p2.shoot(stock)
