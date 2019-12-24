from collections import deque
def main(path):
    with open(path) as infile:
        lines = infile.read().split('\n')
    
    seen = set()
    
    curGen = tuple(tuple(line) for line in lines)
    width = len(curGen[0])
    height = len(curGen)
    
    def inRange(x,y):
        return x>= 0 and x < width and y >= 0 and y < height
    dy=(-1, 0, 1, 0)
    dx=(0,1,0,-1)
    
    def nNeighbour(x,y):
        count = 0
        for i,_ in enumerate(dy):
            nx, ny = x+dx[i], y+dy[i]
            if(inRange(nx,ny)):
                if(curGen[ny][nx] == "#"):
                    count += 1
        return count
        
    def nextCell(x,y):
        count = nNeighbour(x,y)
        if(curGen[y][x] == '#'):
            return '#' if (count == 1) else '.'
        else:
            return '#' if (count == 1 or count == 2) else '.'
    
    seen.add(curGen)
    gen = 0
    
    def bioRate(gen):
        val = 0
        for y in range(height):
            for x in range(width):
                if(gen[y][x] == '#'):
                    val += 2**(x+y*width)
        return val
    
    
    while(True):
        nextGen = tuple(tuple(nextCell(x,y) for x in range(width)) for y in range(height))
        
        if(nextGen not in seen):
            seen.add(nextGen)
            curGen = nextGen
        else:
            break
        gen += 1
    print(bioRate(nextGen))
    
    
    
    

        
    grid = [[list(line) for line in lines]]
    grid[0][2][2] = '?'
    
    def getNextWithLevel(newGen, level, x, y, grid):
        if((x,y) == (2,2)):
            return "?"
        count = 0
        for i in range(4):
            nl = level
            nx = x +dx[i]
            ny = y +dy[i]
            if((nx, ny) != (2, 2)):
                if(nx == -1):
                    nl, nx, ny = nl-1, 1, 2
                elif(ny == -1):
                    nl, nx, ny = nl-1, 2, 1
                elif(nx == width):
                    nl, nx, ny = nl-1, 3, 2
                elif(ny == height):
                    nl, nx, ny = nl-1, 2, 3
                if(nl >= 0):
                    if(grid[nl][ny][nx] == '#'):
                        count += 1
            else:
                nl = level + 1
                if(nl < len(grid)):
                    if(i == 0):
                        #Find bottom row
                        for i in range(width):
                            if(grid[nl][height-1][i] == '#'):
                                count += 1
                    elif(i == 1):
                        #Find left column
                        for i in range(height):
                            if(grid[nl][i][0] == '#'):
                                count += 1
                    elif(i==2):
                        #Find top row
                        #print("Calculating top row")
                        for i in range(width):
                            if(grid[nl][0][i] == '#'):
                                count += 1
                    elif(i==3):
                        #Find right column
                        for i in range(height):
                                if(grid[nl][i][width-1] == '#'):
                                    count += 1
        
        if(grid[level][y][x] == '#'):
            return '#' if (count == 1) else '.'
        else:
            return '#' if (count == 1 or count == 2) else '.'
                
    
    def deepCopy(grids):
        return [ [row[:] for row in grid] for grid in grids]
    for newGen in range(1,201):
        if(newGen%2 == 1):
            extraGrid = [[['.' for _ in range(width)] for _ in range(height)]]
            grid = extraGrid + grid
            grid.append(extraGrid[0])
        nextGrid = [[[ getNextWithLevel(newGen, level, x, y, grid) for x in range(width)] for y in range(height)] for level in range(len(grid))]
        grid = nextGrid
        
    nBugs = 0
    for g in grid:
        for row in g:
            for char in row:
                if char == '#':
                    nBugs += 1
    print(nBugs)
    