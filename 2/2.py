def main(path):
    with open(path) as infile:
        line = infile.read().split(',')
        
    commands = list(map(int, line))

    cmd1 = commands[:]
    cmd1[1]=12
    cmd1[2]=2

    for i in range(0, len(commands), 4):
        opcode = cmd1[i]
        if(opcode == 99):
            break
        if(opcode == 1):
            cmd1[cmd1[i+3]] = cmd1[cmd1[i+1]]+cmd1[cmd1[i+2]]
        elif(opcode == 2):
            cmd1[cmd1[i+3]] = cmd1[cmd1[i+1]]*cmd1[cmd1[i+2]]
    print(cmd1[0])

    for noun in range(100):
        for verb in range(100):
            cmd2 = commands[:]
            cmd2[1] = noun
            cmd2[2] = verb
            for i in range(0, len(commands), 4):
                opcode = cmd2[i]
                if(opcode == 99):
                    break
                if(opcode == 1):
                    cmd2[cmd2[i+3]] = cmd2[cmd2[i+1]]+cmd2[cmd2[i+2]]
                elif(opcode == 2):
                    cmd2[cmd2[i+3]] = cmd2[cmd2[i+1]]*cmd2[cmd2[i+2]]
            if(cmd2[0] == 19690720):
                print(noun*100 + verb)
                break