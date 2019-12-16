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
    
    def run():
        curPC = 0
        cmd = commands[:]
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
                print("ERROR")
                return output
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
    output = run()
    blocks = [[] for i in range(5)]
    minx = 1e100
    maxx = -1e100
    miny = 1e100
    maxy = -1e100
    for i in range(0, len(output), 3):
        blocks[output[i+2]].append((output[i], output[i+1]))
        minx = min(minx, output[i])
        maxx = max(maxx, output[i])
        miny = min(miny, output[i+1])
        maxy = max(maxy, output[i+1])
    print(len(blocks[2]))
    
    board = [[' ' for _ in range(minx, maxx+1)] for _ in range(miny, maxy+1)]
    tiles = [' ', '#', '=', '-', 'o']
    score = -1
    '''
    for i in range(0, len(output), 3):
        if(output[i] == -1 and output[i+1] == 0):
            score = output[i+2]
        else:
            board[output[i+1]][output[i]] = tiles[output[i+2]]
    '''
    
    def print_board():
        for line in board:
            print(''.join(line))
       
    
    def play(input):
        curPC = 0
        cmd = commands[:]
        cmd[0] = 2
        output = []
        relbase = 0
        ball_loc = (-1, -1)
        paddle_loc = (-1, -1)
        lockedOn = False
        score = 0
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

                value = 0
                if(lockedOn):
                    if(ball_loc[0] > paddle_loc[0]):
                        value = 1
                    elif(ball_loc[0] < paddle_loc[0]):
                        value = -1

                if(len(input)==0):
                    cmd[ed] = value
                else:
                    cmd[ed] = input.popleft()
                curPC += 2
            elif(opcode == 4):
                #OUTPUT
                s = cmd[curPC+1]
                val = getVal(cmd, addressMode%10, s, relbase)
                output.append(val)
                
                if(len(output) == 3):
                    if(output[0] == -1 and output[1] == 0):
                        score = output[2]
                    else:
                        board[output[1]][output[0]] = tiles[output[2]]
                        if(output[2] == 4):
                            ball_loc = (output[0], output[1])
                            if(ball_loc[0] == paddle_loc[0]):
                                lockedOn = True
                        if(output[2] == 3):
                            paddle_loc = (output[0], output[1])
                    output = []
                
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
        return score
    print(play(deque([])))
    