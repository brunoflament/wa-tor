import random

EMPTY_CASE=" "
GRID_LEN=30
THON_CASE="T"
THON_COUNT=6
THON_LIFE=5
SHARK_CASE="S"
SHARK_COUNT=0
SHARK_LIFE=6
NUMBER_OF_TURNS=3

MOVE_CASE = {
    0: (-1, 1),
    1: (0, 1),
    2: (1, 1),
    3: (1, 0),
    4: (1, -1),
    5: (0,-1),
    6: (-1, -1),
    7: (-1, 0)
}

class Thon:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.life = THON_LIFE

    def __repr__(self):
      return THON_CASE
        
class Shark:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.life = SHARK_LIFE

    def __repr__(self):
      return SHARK_CASE
    
def print_grid(grid):
    # Parcourir hauteur de la grille
    for line in grid:
        # Parcourir longueur de la grille
        for element in line:
            print(str(element), end="")
            print(" ", end="")
        print()

def add_random_thons(grid, thon_count):
    thons = []
    for i in range(thon_count):
        x = random.randint(0, len(grid)-1)
        y = random.randint(0, len(grid)-1)
        while grid[x][y] is not EMPTY_CASE:
            x = random.randint(0, len(grid)-1)
            y = random.randint(0, len(grid)-1)
        grid[x][y] = Thon(x,y)
        thons.append(grid[x][y])
    return thons

def move_thon(grid, thon):
    while True:
        random_number = random.randint(0, 7)
        new_x = thon.x + MOVE_CASE[random_number][0]
        new_y = thon.y + MOVE_CASE[random_number][1]
        if (new_x < 0 or new_x >= GRID_LEN or new_y < 0 or new_y >= GRID_LEN):
            continue
        elif grid[new_x][new_y] is not EMPTY_CASE:
            continue
        else:
            break
    # print("debug: " +  str(thon.x) + ", " + str(thon.y) + " -> " +  str(new_x) + ", " + str(new_y))
    grid[thon.x][thon.y] = EMPTY_CASE 
    grid[new_x][new_y] = Thon(new_x, new_y)

def thons_list(grid):
    thons = []
    for line in grid:
        for element in line:
            if str(element) == THON_CASE:
                thons.append(element)
    return thons

def add_random_sharks(grid, shark_count):
    sharks = []
    for i in range(shark_count):
        x = random.randint(0, len(grid)-1)
        y = random.randint(0, len(grid)-1)
        while grid[x][y] is not EMPTY_CASE:
            x = random.randint(0, len(grid)-1)
            y = random.randint(0, len(grid)-1)
        grid[x][y] = Shark(x,y)
        sharks.append(grid[x][y])
    return sharks

if __name__ == "__main__":
    ## Creation d'une grille vide
    grid = [[EMPTY_CASE for x in range(GRID_LEN)] for y in range(GRID_LEN)]
    ## J'ajoute des thons dans ma grille
    thons = add_random_thons(grid,THON_COUNT)
    ## J'ajoute des requins dans ma grille
    sharks = add_random_sharks(grid,SHARK_COUNT)
    ## J'affiche la grille
    print_grid(grid)
    print('-'*GRID_LEN*2)

    ## GAME
    t = 0
    while t < NUMBER_OF_TURNS:
        for thon in thons:
            ## Je déplace un thon dans la grille
            move_thon(grid, thon)
        print_grid(grid)
        print('-'*GRID_LEN*2)
        ## je regénère la liste de thons mis à jour
        thons = thons_list(grid)
        ## J'ajoute 1 tour
        t = t + 1
