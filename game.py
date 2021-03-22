class Grid:
    def __init__(self, size):
        self.size = size
        self.ship = []
        self.shot = []
        self.count = 0
        
    def creating_grid(self):
        alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        num = []
        for i in range(self.size + 1):
            if i < 10:
                num.append("  {}   ".format(i))
            else:
                num.append("  {}  ".format(i))
        self.ship.append(num)
        self.shot.append(num)
        for i in range(1, self.size + 1):
            temp = []
            for t in range(self.size + 1):
                if t == 0:
                    temp.append("  {}  /".format(alpha[i-1]))
                else:
                    temp.append("     /")
            self.ship.append(temp)
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
                print(string)while pmove_count <= ship_size:
                            if prow[pcol] == "     /":
                                continue
                            else:
                                return print("\nShips overlap. Please choose another spot or different direction.")
                            ppot -= 1
                            prow = self.ship[ppot]
                            pmove_count += 1
    
    def create_ship(self, location, direction, ship_size, number):
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
                            if prow[pcol] == "     /":
                                continue
                            else:
                                return print("\nShips overlap. Please choose another spot or different direction.")
                            pcol -= 1
                            pmove_count += 1
                        row[col] = "  {}  /".format(number)
                        self.count += ship_size
                        while move_count < ship_size:
                            col -= 1
                            row[col] = "  {}  /".format(number)
                            move_count += 1
                        self.ship[pot] = row
                    elif direction == "R":
                        while pmove_count <= ship_size:
                            if prow[pcol] == "     /":
                                continue
                            else:
                                return print("\nShips overlap. Please choose another spot or different direction.")
                            pcol += 1
                            pmove_count += 1
                        row[col] = "  {}  /".format(number)
                        self.count += ship_size
                        while move_count < ship_size:
                            col += 1
                            row[col] = "  {}  /".format(number)
                            move_count += 1
                        self.ship[pot] = row
                    elif direction == "U":
                        while pmove_count <= ship_size:
                            if prow[pcol] == "     /":
                                continue
                            else:
                                return print("\nShips overlap. Please choose another spot or different direction.")
                            ppot -= 1
                            prow = self.ship[ppot]
                            pmove_count += 1
                        row[col] = "  {}  /".format(number)
                        self.count += ship_size
                        self.ship[pot] = row
                        while move_count < ship_size:
                            pot -= 1
                            row = self.ship[pot]
                            row[col] = "  {}  /".format(number)
                            self.ship[pot] = row
                            move_count += 1
                    elif direction == "D":
                        while pmove_count <= ship_size:
                            if prow[pcol] == "     /":
                                continue
                            else:
                                return print("\nShips overlap. Please choose another spot or different direction.")
                            ppot += 1
                            prow = self.ship[ppot]
                            pmove_count += 1
                        row[col] = "  {}  /".format(number)
                        self.count += ship_size
                        self.ship[pot] = row
                        while move_count < ship_size:
                            pot += 1
                            row = self.ship[pot]
                            row[col] = "  {}  /".format(number)
                            self.ship[pot] = row
                            move_count += 1
                    else:
                        return print("\nDirection or location is invalid. Please enter a new spot.")



grid = Grid(10)
grid.creating_grid()
grid.print_grid("ship")
grid.create_ship("A9", "R", 3, 1)
grid.print_grid("ship")
