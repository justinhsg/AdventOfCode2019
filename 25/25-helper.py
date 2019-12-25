import sys
with open("items", "r") as infile:
    items = infile.read().split("\n")
    
    
if(len(sys.argv) != 2):
    print("Usage: python 25-helper.py <direction>\n\t <direction> is the direction to enter the Pressure-Sensitive Floor")
else:
    testDirection = sys.argv[1]
    graycode = [[]]
    for _ in enumerate(items):
        secondhalf = [code[:] for code in graycode[::-1]]
        graycode = graycode + secondhalf
        for i in range(len(graycode)//2):
            graycode[i].append(1)
            graycode[i+len(graycode)//2].append(0)
            
    prevState = graycode[0]



    opstring = ""
    opstring = "{}\n".format(testDirection)
    for curState in graycode[1:]:
        for idx,_ in enumerate(curState):
            if(prevState[idx] != curState[idx]):
                opstring += "take {}\n".format(items[idx]) if prevState[idx] == 0 else "drop {}\n".format(items[idx])
        opstring += "{}\n".format(testDirection)
        prevState = curState

    with open("helperout", "w") as outfile:
        outfile.write(opstring)
        