def main(path):
    with open(path) as infile:
        line = infile.read()
    
    intseq = list(map(int, line))
    
    def nextSeq(seq):
        
        newSeq = []
        for i in range(len(seq)):
            val = 0
            period = i+1
            for j in range(i, len(seq), period*4):
        
                val += sum(seq[j:j+period]) - sum(seq[j+period*2: j+period*3])
            val = val%10 if val>0 else (-val)%10
            
            newSeq.append(val)
        return newSeq
    
    curSeq = intseq[:]
    for i in range(100):
        curSeq = nextSeq(curSeq)
    print("".join(map(str, curSeq[:8])))
    

    offset = int("".join(map(str,intseq[:7])))
    longintseq = list(map(int, line))*10000
    truncList = longintseq[offset:]
    
    
    for _ in range(100):
        newlist = []
        prevsum = 0
        for i in range(len(truncList)-1, -1, -1):
            newsum = prevsum + truncList[i]
            prevsum = newsum%10
            newlist.append(prevsum)
        truncList = newlist[::-1]
    print("".join(map(str, truncList[:8])))