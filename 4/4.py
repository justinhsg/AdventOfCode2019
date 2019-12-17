#Combinatorial solution is possible, but this brute forces the solution easily enough
def main(path):
    with open(path) as infile:
        line = infile.read().split('\n')
    start, end = map(int, line[0].split('-'))
    
    
    nValid1 = 0
    nValid2 = 0
    for i in range(start, end+1):
        
        testNo = i
        hasSame = 0
        hasRepeat = False
        strictlyTwice = False
        isMonotonic = True
        lastDigit = 10
        while(testNo != 0):
            curDigit = testNo%10
            if(curDigit == lastDigit):
                hasSame+=1
                hasRepeat = True
            elif(curDigit > lastDigit):
                isMonotonic = False
                break
            else:
                if(hasSame == 1):
                    strictlyTwice = True
                hasSame = 0
            testNo //= 10
            lastDigit = curDigit
        if(hasSame == 1):
            strictlyTwice = True
        if(hasRepeat and isMonotonic):
            nValid1+=1
        if(strictlyTwice and isMonotonic):
            nValid2+=1
    print(nValid1)
    print(nValid2)
            