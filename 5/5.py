def main(path):
    with open(path) as infile:
        line = infile.read().split(',')
        
    commands = list(map(int, line))
    
    
    def execute(input):
        cmd1 = commands[:]
        pc = 0
        while(True):
            instruction = cmd1[pc]
            opcode = instruction%100
            addressMode = instruction//100
            if(opcode == 1):
                s1 = cmd1[pc+1]
                s2 = cmd1[pc+2]
                d = cmd1[pc+3]
                val1 = cmd1[s1] if addressMode%10 == 0 else s1
                val2 = cmd1[s2] if (addressMode//10)%10 == 0 else s2
                cmd1[d] = val1+val2
                pc += 4
            elif(opcode == 2):
                s1 = cmd1[pc+1]
                s2 = cmd1[pc+2]
                d = cmd1[pc+3]
                val1 = cmd1[s1] if addressMode%10 == 0 else s1
                val2 = cmd1[s2] if (addressMode//10)%10 == 0 else s2
                cmd1[d] = val1*val2
                pc += 4
            elif(opcode == 3):
                d = cmd1[pc+1]
                cmd1[d] = input
                pc+=2
            elif(opcode == 4):
                s = cmd1[pc+1]
                val = cmd1[s] if addressMode%10 == 0 else s
                if(val != 0):
                    print(val)
                pc+=2
            elif(opcode == 5):
                s1 = cmd1[pc+1]
                s2 = cmd1[pc+2]
                val1 = cmd1[s1] if addressMode%10 == 0 else s1
                val2 = cmd1[s2] if (addressMode//10)%10 == 0 else s2
                if(val1 != 0):
                    pc = val2
                else:
                    pc += 3
            elif(opcode == 6):
                s1 = cmd1[pc+1]
                s2 = cmd1[pc+2]
                d = cmd1[pc+3]
                val1 = cmd1[s1] if addressMode%10 == 0 else s1
                val2 = cmd1[s2] if (addressMode//10)%10 == 0 else s2
                if(val1 == 0):
                    pc = val2
                else:
                    pc += 3
            elif(opcode == 7):
                s1 = cmd1[pc+1]
                s2 = cmd1[pc+2]
                d = cmd1[pc+3]
                val1 = cmd1[s1] if addressMode%10 == 0 else s1
                val2 = cmd1[s2] if (addressMode//10)%10 == 0 else s2
                cmd1[d] = 1 if val1 < val2 else 0
                pc += 4
            elif(opcode == 8):
                s1 = cmd1[pc+1]
                s2 = cmd1[pc+2]
                d = cmd1[pc+3]
                val1 = cmd1[s1] if addressMode%10 == 0 else s1
                val2 = cmd1[s2] if (addressMode//10)%10 == 0 else s2
                cmd1[d] = 1 if val1 == val2 else 0
                pc += 4
            elif(opcode == 99):
                break
                
    execute(1)
    execute(5)