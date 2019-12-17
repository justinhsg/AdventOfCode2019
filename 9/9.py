from collections import deque
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
    
    def run(input):
        curPC = 0
        cmd = commands[:]
        output = deque()
        relbase = 0
        while(True):
            
            #curPC = pcs[run]
            #cmd = cmds[run]
            
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
    print(run(deque([1]))[0])
    print(run(deque([2]))[0])