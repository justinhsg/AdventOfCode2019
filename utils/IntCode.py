def run(input, commands, pc, base):
    curPC = pc
    cmd = commands[:]
    output = []
    relbase = base
    
    
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
            
            src1 = getSrc(cmd, addressMode%10, s1, relbase)
            src2 = getSrc(cmd, (addressMode//10)%10, s2, relbase)
            des = getDes(cmd, (addressMode//100)%10, d, relbase)

            cmd[des] = src1+src2
            
            curPC += 4
        elif(opcode == 2):
            #MULT
            s1 = cmd[curPC+1]
            s2 = cmd[curPC+2]
            d = cmd[curPC+3]
            
            src1 = getSrc(cmd, addressMode%10, s1, relbase)
            src2 = getSrc(cmd, (addressMode//10)%10, s2, relbase)
            des = getDes(cmd, (addressMode//100)%10, d, relbase)
            
            cmd[des] = src1*src2
            
            curPC += 4
        elif(opcode == 3):
            #INPUT
            d = cmd[curPC+1]            
            des = getDes(cmd, addressMode%10, d, relbase)   
            
            if(len(input)==0):
                return(1, output, cmd, curPC, base)
            else:
                cmd[des] = input.popleft()
                
            curPC += 2
        elif(opcode == 4):
            #OUTPUT
            s = cmd[curPC+1]
            
            src = getSrc(cmd, addressMode%10, s, relbase)
            
            output.append(src)
            
            curPC += 2
        elif(opcode == 5):
            #Jump if True
            s1 = cmd[curPC+1]
            s2 = cmd[curPC+2]
            
            src1 = getSrc(cmd, addressMode%10, s1, relbase)
            src2 = getSrc(cmd, (addressMode//10)%10, s2, relbase)
            
            if(src1 != 0):
                curPC = src2
            else:
                curPC += 3
        elif(opcode == 6):
            #Jump if False
            s1 = cmd[curPC+1]
            s2 = cmd[curPC+2]
            
            src1 = getSrc(cmd, addressMode%10, s1, relbase)
            src2 = getSrc(cmd, (addressMode//10)%10, s2, relbase)
            
            if(src1 == 0):
                curPC = src2
            else:
                curPC += 3
        elif(opcode == 7):
            #LT
            s1 = cmd[curPC+1]
            s2 = cmd[curPC+2]
            d = cmd[curPC+3]
            
            src1 = getSrc(cmd, addressMode%10, s1, relbase)
            src2 = getSrc(cmd, (addressMode//10)%10, s2, relbase)
            des = getDes(cmd, (addressMode//100)%10, d, relbase)
                
            cmd[des] = 1 if src1 < src2 else 0
            
            curPC += 4
        elif(opcode == 8):
            #EQ
            s1 = cmd[curPC+1]
            s2 = cmd[curPC+2]
            d = cmd[curPC+3]
            
            src1 = getSrc(cmd, addressMode%10, s1, relbase)
            src2 = getSrc(cmd, (addressMode//10)%10, s2, relbase)
            des = getDes(cmd, (addressMode//100)%10, d, relbase)
                
            cmd[des] = 1 if src1 == src2 else 0
            
            curPC += 4
        elif(opcode == 9):
            #SETBASE
            s = cmd[curPC+1]
            
            src = getSrc(cmd, addressMode%10, s, relbase)
            
            relbase += src
            
            curPC += 2
        elif(opcode == 99):
            return(0, output, cmd, curPC, base) 