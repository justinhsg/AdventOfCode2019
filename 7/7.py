from collections import deque
def main(path):
    with open(path) as infile:
        line = infile.read().split(',')
        
    commands = list(map(int, line))
    
    def nextPermutation(seq):
        newseq = seq[:]
        k = -1
        for i in range(len(seq)-2, -1, -1):
            if(seq[i] < seq[i+1]):
                k = i
                break
        if(k == -1):
            return []
        else:
            l = -1
            for i in range(len(seq)-1, k, -1):
                if(seq[k] < seq[i]):
                    l = i
                    break
            newseq[k] = seq[l]
            newseq[l] = seq[k]
            newerseq = newseq[:]
            j = len(seq)-1
            for i in range(k+1, len(seq)):
                newerseq[i] = newseq[j]
                j -= 1
        return newerseq
    
    
    def run(seq):
        streams = [deque([seq[i]]) for i in range(5)]
        streams[0].append(0)
        cmds = [commands[:] for _ in range(5)]
        status = [False for _ in range(5)]
        pcs = [0 for _ in range(5)]
        run = 0
        maxPhase = 0
        while(True):
            
            curPC = pcs[run]
            cmd = cmds[run]
            instruction = cmd[curPC]
            opcode = instruction%100
            addressMode = instruction//100
            if(opcode == 1):
                s1 = cmd[curPC+1]
                s2 = cmd[curPC+2]
                d = cmd[curPC+3]
                val1 = cmd[s1] if addressMode%10 == 0 else s1
                val2 = cmd[s2] if (addressMode//10)%10 == 0 else s2
                cmd[d] = val1+val2
                pcs[run] += 4
            elif(opcode == 2):
                s1 = cmd[curPC+1]
                s2 = cmd[curPC+2]
                d = cmd[curPC+3]
                val1 = cmd[s1] if addressMode%10 == 0 else s1
                val2 = cmd[s2] if (addressMode//10)%10 == 0 else s2
                cmd[d] = val1*val2
                pcs[run] += 4
            elif(opcode == 3):
                d = cmd[curPC+1]
                if(len(streams[run]) == 0):

                    run = (run+1)%5
                else:
                    cmd[d] = streams[run].popleft()
                    pcs[run] += 2
            elif(opcode == 4):
                s = cmd[curPC+1]
                val = cmd[s] if addressMode%10 == 0 else s
                streams[(run+1)%5].append(val)
                if(run == 4):
                    maxPhase = max(maxPhase, val)
                pcs[run] += 2
            elif(opcode == 5):
                s1 = cmd[curPC+1]
                s2 = cmd[curPC+2]
                val1 = cmd[s1] if addressMode%10 == 0 else s1
                val2 = cmd[s2] if (addressMode//10)%10 == 0 else s2
                if(val1 != 0):
                    pcs[run] = val2
                else:
                    pcs[run] += 3
            elif(opcode == 6):
                s1 = cmd[curPC+1]
                s2 = cmd[curPC+2]
                d = cmd[curPC+3]
                val1 = cmd[s1] if addressMode%10 == 0 else s1
                val2 = cmd[s2] if (addressMode//10)%10 == 0 else s2
                if(val1 == 0):
                    pcs[run] = val2
                else:
                    pcs[run] += 3
            elif(opcode == 7):
                s1 = cmd[curPC+1]
                s2 = cmd[curPC+2]
                d = cmd[curPC+3]
                val1 = cmd[s1] if addressMode%10 == 0 else s1
                val2 = cmd[s2] if (addressMode//10)%10 == 0 else s2
                cmd[d] = 1 if val1 < val2 else 0
                pcs[run] += 4
            elif(opcode == 8):
                s1 = cmd[curPC+1]
                s2 = cmd[curPC+2]
                d = cmd[curPC+3]
                val1 = cmd[s1] if addressMode%10 == 0 else s1
                val2 = cmd[s2] if (addressMode//10)%10 == 0 else s2
                cmd[d] = 1 if val1 == val2 else 0
                pcs[run] += 4
            elif(opcode == 99):
                if(run == 4):
                    break
                run = (run+1)%5     
        
        return maxPhase
        
    seq = [0,1,2,3,4]
    maxPhase = 0
    maxSeq = []
    while(seq != []):
        output = run(seq)
        if(output > maxPhase):
            maxPhase = output
            maxSeq = seq
        seq = nextPermutation(seq)
        
    print(maxPhase, maxSeq)
    
    
    seq = [5,6,7,8,9]
    maxPhase = 0
    maxSeq = []
    while(seq != []):
        output = run(seq)
        if(output > maxPhase):
            maxPhase = output
            maxSeq = seq
        seq = nextPermutation(seq)
        
    print(maxPhase, maxSeq)