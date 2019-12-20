from collections import deque
from utils import pair, IntCode
def main(path):
    with open(path) as infile:
        line = infile.read().split(',')
        
    commands = list(map(int, line))
    
    def runIntCode(input, clean):
        newCommands = commands[:]
        if(clean):
            newCommands[0] = 2
        result = IntCode.run(input, newCommands, 0, 0)
        if(result[0] == 1):
            return None
        else:
            return result[1]
    
    output = runIntCode(deque([]), False)
    
    view = []
    row = []
    for char in output:
        if(char == 10):
            view.append(row)
            row = []
        else:
            row.append(chr(char))
    
    start = (-1, -1)
    for y in range(len(view)):
        for x in range(len(view[y])):
            if(view[y][x] in '^v<>'):
                start = (x, y)
                break

    parsum = 0
    for y in range(1,len(view)-2):
        for x in range(1,len(view[y])-1):
            if(view[y][x] == '#'):
                if(view[y-1][x] == '#' and view[y+1][x] == '#' and view[y][x-1] == '#' and view[y][x+1]=='#'):
                    parsum += x*y
    print(parsum)
    
    
    
    
    instructions = []
    dy=(-1, 0, 1, 0)
    dx=(0, 1, 0, -1)
    face = 0
    curX, curY = start
    
    def inRange(x, y):
        return x >= 0 and x < len(view[0]) and y >= 0 and y < len(view)-1
    
    def hasPathForward(x,y, face):
        tryX = x + dx[face]
        tryY = y + dy[face]
        if(inRange(tryX, tryY)):
            if(view[tryY][tryX] == '#'):
                return True
        return False
    
    while(True):
        hasProgress = False
        for i in [0,1,-1]:
            newFace = (face+i)%4
            if(hasPathForward(curX, curY, newFace)):
                hasProgress = True
                if(i==0):
                    instructions[-1] += 1
                elif(i==1):
                    instructions.append('R')
                    instructions.append(1)
                    face = newFace
                elif(i==-1):
                    instructions.append('L')
                    instructions.append(1)
                    face = newFace
                face = newFace
                curX += dx[face]
                curY += dy[face]
                break
        if(not hasProgress):
            break
            
    asString = ",".join(list(map(str, instructions)))
    
    curPos = 0
    A = ""
    B = ""
    C = ""
    seq = ""
    found = False
    for Alen in range(1,21):
        if(found):
            break
        for Blen in range(1,21):
            if(found):
                break
            for Clen in range(1,21):
                if(found):
                    break
                curPos = 0
                seq = ""
                A = asString[curPos: curPos+Alen]
                if(A[0] == ',' or A[-1] == ','):
                    continue
                while(True):
                    if(asString[curPos:curPos+Alen] == A):
                        curPos += (Alen+1)
                        seq += ",A"
                    else:
                        break
                B = asString[curPos: curPos+Blen]
                
                if(B[0] == ',' or B[-1] == ','):
                    continue
                while(True):
                    if(asString[curPos:curPos+Alen] == A):
                        curPos += (Alen+1)
                        seq += ",A"
                    elif(asString[curPos:curPos+Blen] == B):
                        curPos += (Blen+1)
                        seq += ",B"
                    else:
                        break
                C = asString[curPos: curPos+Clen]
                
                if(C[0] == ',' or C[-1] == ','):
                    continue
                while(True):
                    if(asString[curPos:curPos+Alen] == A):
                        curPos += (Alen+1)
                        seq += ",A"
                    elif(asString[curPos:curPos+Blen] == B):
                        curPos += (Blen+1)
                        seq += ",B"
                    elif(asString[curPos:curPos+Clen] == C):
                        curPos += (Clen+1)
                        seq += ",C"
                    else:
                        break
                if(curPos == len(asString)+1):
                    found = True           
                    
    seqInput = list(map(ord,list(seq[1:])))
    seqInput.append(10)
    aInput = list(map(ord,list(A)))
    aInput.append(10)
    bInput = list(map(ord,list(B)))
    bInput.append(10)
    cInput = list(map(ord,list(C)))
    cInput.append(10)
    
    fullInput = deque(seqInput + aInput + bInput + cInput + [ord('n'), 10])
    fullOutput = runIntCode(fullInput, True)

    print(fullOutput[-1])
