import random

class World:
    def __init__(self, width=30, height=15, seed=None):
        self.width = width
        self.height = height
        self.seed = seed
        if seed:
            random.seed(seed)
        self.map = []
        self.generate_world()

    def generate_world(self):
        self.map = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(self.generate_tile())
            self.map.append(row)

        self.place_towns(5)
        self.place_player()

    def generate_tile(self):
        roll = random.randint(1, 100)

        if roll <= 15:
            return "~"  # Water
        elif roll <= 35:
            return "T"  # Forest
        elif roll <= 50:
            return "^"  # Mountain
        else:
            return "."  # Plains

    def place_towns(self, count):
        placed = 0
        while placed < count:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)

            if self.map[y][x] == ".":
                self.map[y][x] = "#"
                placed += 1

    def place_player(self):
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)

            if self.map[y][x] == ".":
                self.player_x = x
                self.player_y = y
                break

    def display(self):
        print("\n=== Procedural World ===\n")
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                if x == self.player_x and y == self.player_y:
                    row += "P "
                else:
                    row += self.map[y][x] + " "
            print(row)

    def move_player(self, direction):
        dx, dy = 0, 0

        if direction == "w":
            dy = -1
        elif direction == "s":
            dy = 1
        elif direction == "a":
            dx = -1
        elif direction == "d":
            dx = 1

        new_x = self.player_x + dx
        new_y = self.player_y + dy

        if 0 <= new_x < self.width and 0 <= new_y < self.height:
            if self.map[new_y][new_x] != "~":
                self.player_x = new_x
                self.player_y = new_y

    def legend(self):
        print("\nLegend:")
        print("P  Player")
        print("~  Water")
        print("T  Forest")
        print("^  Mountain")
        print(".  Plains")
        print("#  Town")


def main():
    seed = input("Enter seed (or press Enter for random world): ")

    if seed.strip() == "":
        world = World()
    else:
        world = World(seed=seed)

    while True:
        world.display()
        world.legend()

        move = input("\nMove (WASD) or Q to quit: ").lower()

        if move == "q":
            break

        if move in ["w", "a", "s", "d"]:
            world.move_player(move)


if __name__ == "__main__":
    main()
