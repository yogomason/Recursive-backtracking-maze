from random import randint

class node:

    def __init__(self, id):
        self.id = id
        self.paths = []
        self.visited = False
    
    def visit(self):
        self.visited = True
    
    def __str__(self):
        return self.id

class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        self.stack.pop()

    def push(self, i):
        self.stack.append(i)

    def status(self):
        if len(self.stack) > 0:
            return True
        else:
            return False

# def buildgrid(dimensions):
#     grid = []
#     for i in range(1, 26, 5):
#         grid.append([node(i),node(i+1),node(i+2),node(i+3),node(i+4)])
#     return(grid)

def buildgrid(dimensions):
    grid = []
    row = []
    for i in range(1, (dimensions * dimensions)+1):
        row.append(node(i))
        if i % dimensions == 0:
            grid.append(row)
            row = []
    return(grid)

grid = buildgrid(4)
visualgrid = [
    ['#', '-','#', '-','#', '-','#', '-','#'],
    ['#', '#','#', '#','#', '#','#', '#','#'],
    ['#', '-','#', '-','#', '-','#', '-','#'],
    ['#', '#','#', '#','#', '#','#', '#','#'],
    ['#', '-','#', '-','#', '-','#', '-','#'],
    ['#', '#','#', '#','#', '#','#', '#','#'],
    ['#', '-','#', '-','#', '-','#', '-','#'],
    ['#', '#','#', '#','#', '#','#', '#','#'],
    ]


def buildmaze(grid, x, y, prev = None):
    global visualgrid
    grid[x][y].visit()
    if prev is not None:
        grid[x][y].paths.append(prev)
    while True:
        newx, newy = findnext(grid, x, y)
        if newx == None or newy == None:
            return
        grid[x][y].paths.append(grid[newx][newy])
        buildmaze(grid, newx, newy, grid[x][y])




def findnext(grid, x, y):
    if x == 0 and y == 0:
        newx, newy = searchrd(grid, x, y)
    elif x == len(grid)-1 and y == 0:
        newx, newy = searchru(grid, x, y)
    elif x == len(grid)-1 and y == len(grid)-1:
        newx, newy = searchlu(grid, x, y)
    elif x == 0 and y == len(grid)-1:
        newx, newy = searchld(grid, x, y)
    elif x == 0:
        newx, newy = searchldr(grid, x, y)
    elif x == len(grid)-1:
        newx, newy = searchlur(grid, x, y)
    elif y == len(grid)-1:
        newx, newy = searchldu(grid, x, y)
    elif y == 0:
        newx, newy = searchrdu(grid, x, y)
    else:
        newx, newy = searchldur(grid, x, y)
    return newx, newy

def searchrdu(grid, x, y):
    if grid[x+1][y].visited == True and grid[x-1][y].visited == True and grid[x][y+1].visited == True:
        return None, None
    while True:
        i = randint(1,3)
        if i == 1:
            if grid[x][y+1].visited == True:
                pass
            else:
                return x, y+1
        if i == 2:
            if grid[x+1][y].visited == True:
                pass
            else:
                return x+1, y
        if i == 3:
            if grid[x-1][y].visited == True:
                pass
            else:
                return x-1, y

def searchldu(grid, x, y):
    if grid[x][y-1].visited == True and grid[x+1][y].visited == True and grid[x-1][y].visited == True:
        return None, None
    while True:
        i = randint(1,3)
        if i == 1:
            if grid[x-1][y].visited == True:
                pass
            else:
                return x-1, y
        if i == 2:
            if grid[x+1][y].visited == True:
                pass
            else:
                return x+1, y
        if i == 3:
            if grid[x][y-1].visited == True:
                pass
            else:
                return x, y-1

def searchldr(grid, x, y):
    if grid[x][y+1].visited == True and grid[x][y-1].visited == True and grid[x+1][y].visited == True:
        return None, None
    while True:
        i = randint(1,3)
        if i == 1:
            if grid[x+1][y].visited == True:
                pass
            else:
                return x+1, y
        if i == 2:
            if grid[x][y+1].visited == True:
                pass
            else:
                return x, y+1
        if i == 3:
            if grid[x][y-1].visited == True:
                pass
            else:
                return x, y-1

def searchlur(grid, x, y):
    if grid[x-1][y].visited == True and grid[x][y+1].visited == True and grid[x][y-1].visited == True:
        return None, None
    while True:
        i = randint(1,3)
        if i == 1:
            if grid[x-1][y].visited == True:
                pass
            else:
                return x-1, y
        if i == 2:
            if grid[x][y-1].visited == True:
                pass
            else:
                return x, y-1
        if i == 3:
            if grid[x][y+1].visited == True:
                pass
            else:
                return x, y+1


######## for the corners ############

def searchru(grid, x, y):
    if grid[x-1][y].visited == True and grid[x][y+1].visited == True:
        return None, None
    while True:
        i = randint(1,2)
        if i == 1:
            if grid[x-1][y].visited == True:
                pass
            else:
                return x-1, y
        if i == 2:
            if grid[x][y+1].visited == True:
                pass
            else:
                return x, y+1

def searchrd(grid, x, y):
    if grid[x+1][y].visited == True and grid[x][y+1].visited == True:
        return None, None
    while True:
        i = randint(1,2)
        if i == 1:
            if grid[x+1][y].visited == True:
                pass
            else:
                return x+1, y
        if i == 2:
            if grid[x][y+1].visited == True:
                pass
            else:
                return x, y+1##############

def searchld(grid, x, y):
    if grid[x+1][y].visited == True and grid[x][y-1].visited == True:
        return None, None
    while True:
        i = randint(1,2)
        if i == 1:
            if grid[x+1][y].visited == True:
                pass
            else:
                return x+1, y
        if i == 2:
            if grid[x][y-1].visited == True:
                pass
            else:
                return x, y-1

def searchlu(grid, x, y):
    if grid[x-1][y].visited == True and grid[x][y-1].visited == True:
        return None, None
    while True:
        i = randint(1,2)
        if i == 1:
            if grid[x-1][y].visited == True:
                pass
            else:
                return x-1, y
        if i == 2:
            if grid[x][y-1].visited == True:
                pass
            else:
                return x, y-1

####################

def searchldur(grid, x, y):
    if grid[x+1][y].visited == True and grid[x][y+1].visited == True and grid[x-1][y].visited == True and grid[x][y-1].visited == True:
        return None, None
    while True:
        i = randint(1,4)
        if i == 1:
            if grid[x-1][y].visited == True:
                pass
            else:
                return x-1, y
        if i == 2:
            if grid[x][y+1].visited == True:
                pass
            else:
                return x, y+1
        if i == 3:
            if grid[x+1][y].visited == True:
                pass
            else:
                return x+1, y
        if i == 4:
            if grid[x][y-1].visited == True:
                pass
            else:
                return x, y-1



buildmaze(grid, 0, 0)

