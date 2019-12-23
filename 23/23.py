from collections import deque
from utils import IntCode
def main(path):
    with open(path) as infile:
        line = infile.read().split(',')
        
    commands = list(map(int, line))
    
    cmds = [commands[:] for _ in range(50)]
    pcs = [0 for _ in range(50)]
    bases = [0 for _ in range(50)]
    inputs = [deque([i]) for i in range(50)]
    outputs = [deque([]) for i in range(50)]
    term = [False for _ in range(50)]
    
    natX = None
    natY = None
    lastNatY = None
    
    def getSrc(cmd, addressMode, s, relbase):
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
    
    toTerm = True
    while(True):
        for c in range(50):
            if(term[c]):
                continue
            toTerm = False
            cmd = cmds[c]
            curPC = pcs[c]
            relbase = bases[c]
            input = inputs[c]
            output = outputs[c]
            
            instruction = cmd[curPC]
            opcode = instruction%100
            addressMode = instruction//100
            
            
            if(opcode == 1):
                #ADD
                s1 = cmd[curPC+1]
                s2 = cmd[curPC+2]
                d = cmd[curPC+3]
                
                src1 = getSrc(cmd, addressMode%10, s1, relbase)
                src2 = getSrc(cmd, (addressMode//10)%10, s2, relbase)
                des = getDes(cmd, (addressMode//100)%10, d, relbase)

                cmd[des] = src1+src2
                
                pcs[c] += 4
            elif(opcode == 2):
                #MULT
                s1 = cmd[curPC+1]
                s2 = cmd[curPC+2]
                d = cmd[curPC+3]
                
                src1 = getSrc(cmd, addressMode%10, s1, relbase)
                src2 = getSrc(cmd, (addressMode//10)%10, s2, relbase)
                des = getDes(cmd, (addressMode//100)%10, d, relbase)
                
                cmd[des] = src1*src2
                
                pcs[c] += 4
            elif(opcode == 3):
                #INPUT
                d = cmd[curPC+1]            
                des = getDes(cmd, addressMode%10, d, relbase)   
                
                
                
                if(len(input)!=0):
                    cmd[des] = input.popleft()
                else:
                    if(c == 0 and sum(map(len, inputs)) == 0 and natX != None and natY != None):
                        if(natY == lastNatY):
                            print(natY)
                            toTerm = True
                            break
                        cmd[des] = natX
                        input.append(natY)
                        lastNatY = natY
                    else:
                        cmd[des] = -1
                
                pcs[c] += 2
            elif(opcode == 4):
                #OUTPUT
                s = cmd[curPC+1]
                
                src = getSrc(cmd, addressMode%10, s, relbase)
                
                output.append(src)
                if(len(output) == 3):
                    dc = output.popleft()
                    x = output.popleft()
                    y = output.popleft()
                    if(dc == 255):
                        if(natY == None):
                            print(y)
                        natX = x
                        natY = y
                    else:
                        inputs[dc].append(x)
                        inputs[dc].append(y)
                    
                   
                
                pcs[c] += 2
            elif(opcode == 5):
                #Jump if True
                s1 = cmd[curPC+1]
                s2 = cmd[curPC+2]
                
                src1 = getSrc(cmd, addressMode%10, s1, relbase)
                src2 = getSrc(cmd, (addressMode//10)%10, s2, relbase)
                
                if(src1 != 0):
                    pcs[c] = src2
                else:
                    pcs[c] += 3
            elif(opcode == 6):
                #Jump if False
                s1 = cmd[curPC+1]
                s2 = cmd[curPC+2]
                
                src1 = getSrc(cmd, addressMode%10, s1, relbase)
                src2 = getSrc(cmd, (addressMode//10)%10, s2, relbase)
                
                if(src1 == 0):
                    pcs[c] = src2
                else:
                    pcs[c] += 3
            elif(opcode == 7):
                #LT
                s1 = cmd[curPC+1]
                s2 = cmd[curPC+2]
                d = cmd[curPC+3]
                
                src1 = getSrc(cmd, addressMode%10, s1, relbase)
                src2 = getSrc(cmd, (addressMode//10)%10, s2, relbase)
                des = getDes(cmd, (addressMode//100)%10, d, relbase)
                    
                cmd[des] = 1 if src1 < src2 else 0
                
                pcs[c] += 4
            elif(opcode == 8):
                #EQ
                s1 = cmd[curPC+1]
                s2 = cmd[curPC+2]
                d = cmd[curPC+3]
                
                src1 = getSrc(cmd, addressMode%10, s1, relbase)
                src2 = getSrc(cmd, (addressMode//10)%10, s2, relbase)
                des = getDes(cmd, (addressMode//100)%10, d, relbase)
                    
                cmd[des] = 1 if src1 == src2 else 0
                
                pcs[c] += 4
            elif(opcode == 9):
                #SETBASE
                s = cmd[curPC+1]
                
                src = getSrc(cmd, addressMode%10, s, relbase)
                
                bases[c] += src
                
                pcs[c] += 2
            elif(opcode == 99):
                term[c] = True
            
            if(toTerm):
                break
        if(toTerm):
            break
    
    