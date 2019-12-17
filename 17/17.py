from collections import deque
from utils import pair
def main(path):
    with open(path) as infile:
        line = infile.read().split(',')
        
    commands = list(map(int, line))
    
    def getVal(cmd, addressMode, s, relbase):
        if (addressMode == 0):
            if(s >= len(cmd)):
                cmd += [0 for _ in range(s-len(cmd)+1)]
            return cmd[s]
        elif (addressMode == 1):
            return s
        elif (addressMode == 2):
            if(relbase+s >= len(cmd)):
                cmd += [0 for _ in range(relbase+s-len(cmd)+1)]
            return cmd[relbase+s]
    
    def getDes(cmd, addressMode, d, relbase):
        if (addressMode == 0):
            if(d >= len(cmd)):
                cmd+=[0 for _ in range(d-len(cmd)+1)]
            return d
        elif (addressMode == 2):
            if(relbase+d >= len(cmd)):
                cmd+=[0 for _ in range(relbase+d-len(cmd)+1)]
            return relbase+d
    
    def run(input, clean):
        curPC = 0
        cmd = commands[:]
        if(clean):
            cmd[0] = 2
        output = []
        relbase = 0
        while(True):
            instruction = cmd[curPC]
            if(instruction == 0):
                break
            opcode = instruction%100
            addressMode = instruction//100
            
            
            if(opcode == 1):
                #ADD
                s1 = cmd[curPC+1]
                s2 = cmd[curPC+2]
                d = cmd[curPC+3]
                val1 = getVal(cmd, addressMode%10, s1, relbase)
                val2 = getVal(cmd, (addressMode//10)%10, s2, relbase)
                ed = getDes(cmd, (addressMode//100)%10, d, relbase)

                cmd[ed] = val1+val2
                curPC += 4
            elif(opcode == 2):
                #MULT
                s1 = cmd[curPC+1]
                s2 = cmd[curPC+2]
                d = cmd[curPC+3]
                val1 = getVal(cmd, addressMode%10, s1, relbase)
                val2 = getVal(cmd, (addressMode//10)%10, s2, relbase)
                ed = getDes(cmd, (addressMode//100)%10, d, relbase)
                
                cmd[ed] = val1*val2
                curPC += 4
            elif(opcode == 3):
                #INPUT
                d = cmd[curPC+1]            
                ed = getDes(cmd, addressMode%10, d, relbase)    
                if(len(input)==0):
                    return output
                else:
                    cmd[ed] = input.popleft()
                curPC += 2
            elif(opcode == 4):
                #OUTPUT
                s = cmd[curPC+1]
                val = getVal(cmd, addressMode%10, s, relbase)
                output.append(val)
                curPC += 2
            elif(opcode == 5):
                #Jump if True
                s1 = cmd[curPC+1]
                s2 = cmd[curPC+2]
                
                val1 = getVal(cmd, addressMode%10, s1, relbase)
                val2 = getVal(cmd, (addressMode//10)%10, s2, relbase)
                
                if(val1 != 0):
                    curPC = val2
                else:
                    curPC += 3
            elif(opcode == 6):
                #Jump if false
                s1 = cmd[curPC+1]
                s2 = cmd[curPC+2]
                
                val1 = getVal(cmd, addressMode%10, s1, relbase)
                val2 = getVal(cmd, (addressMode//10)%10, s2, relbase)
                
                if(val1 == 0):
                    curPC = val2
                else:
                    curPC += 3
            elif(opcode == 7):
                #LT
                s1 = cmd[curPC+1]
                s2 = cmd[curPC+2]
                d = cmd[curPC+3]
                
                val1 = getVal(cmd, addressMode%10, s1, relbase)
                val2 = getVal(cmd, (addressMode//10)%10, s2, relbase)
                ed = getDes(cmd, (addressMode//100)%10, d, relbase)
                    
                cmd[ed] = 1 if val1 < val2 else 0
                curPC += 4
            elif(opcode == 8):
                #EQ
                s1 = cmd[curPC+1]
                s2 = cmd[curPC+2]
                d = cmd[curPC+3]
                
                val1 = getVal(cmd, addressMode%10, s1, relbase)
                val2 = getVal(cmd, (addressMode//10)%10, s2, relbase)
                ed = getDes(cmd, (addressMode//100)%10, d, relbase)
                
                    
                cmd[ed] = 1 if val1 == val2 else 0
                curPC += 4
            elif(opcode == 9):
                #SETBASE
                s = cmd[curPC+1]
                
                val = getVal(cmd, addressMode%10, s, relbase)
                
                relbase += val
                curPC += 2
            elif(opcode == 99):
                break   
        return output
    
    output = run(deque([]), False)
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
    fullOutput = run(fullInput, True)
    print(fullOutput[-1])
