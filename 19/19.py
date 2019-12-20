from collections import deque
from utils import IntCode
def main(path):
    with open(path) as infile:
        line = infile.read().split(',')
        
    commands = list(map(int, line))
    
    
    def runIntCode(input):
        result = IntCode.run(input, commands, 0, 0)
        if(result[0] == 1):
            return None
        else:
            return result[1][0]
    
    nPulled = 0
    for y in range(50):
        for x in range(50):
            output = runIntCode(deque([x, y]))
            if(output == 1):
                nPulled += 1
    print(nPulled)
    
    
    lastEnd = 7
    curY = 6

    BOX_SIZE = 100
    while(True):
        
        nextEnd = lastEnd
        while(runIntCode(deque([nextEnd, curY])) == 1):
            nextEnd += 1
        lastEnd = nextEnd
        
        if(lastEnd > BOX_SIZE):
            corners = ( (lastEnd-BOX_SIZE, curY), \
                        (lastEnd-BOX_SIZE, curY+BOX_SIZE-1),\
                        (lastEnd-1,     curY+BOX_SIZE-1) )
            fits = True
            for (x,y) in corners:
                if(runIntCode(deque([x,y])) == 0):
                    fits = False
                    break
            if(fits):
                print(corners[0][0]*10000 + corners[0][1])
                break
        curY += 1