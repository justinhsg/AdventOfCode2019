from collections import deque
from utils import IntCode
def main(path):
    with open(path) as infile:
        line = infile.read().split(',')
        
    commands = list(map(int, line))
    
    def runIntCode(input):
        
        term, output, newcmd, newPC, newBase = IntCode.run(input, commands, 0, 0)
        return output
        
    def toAscii(arr):
        return "".join(map(chr, arr))
    
    def fromAscii(str):
        return(deque(map(ord, list(str))))
    
    
    
    print("====Special Instructions for Day 25=====")
    print("\t 1. For the first bit of the problem, manually navigate the maze with the interactive CLI")
    print("\t 2. Keep track of your route in ./25/cmds. The goal is to reach the checkpoint with all valid items")
    print("\t \t (2a. If you run this program again you should be just before the checkpoint with all items with you)")
    print("\t 3. Edit ./25/items to include the all collectable items")
    print("\t 4. Run ./25/25.helper to produce ./25/helperout")
    print("\t 5. Run this program again without the interactive CLI") 
    print("For an interactive CLI, type Y, else type N. (Use 'q' to exit the CLI)")
    
    interactive = (input()=="Y")
    
    textInput = ""
    
    with open("./25/cmds") as infile:
        textInput = infile.read()
    
    with open("./25/helperout") as infile:
        if(textInput[-1] == "\n"):
            textInput += infile.read()
        else:
            textInput += "\n" + infile.read()
    
    if(textInput[-1] != "\n"):
        textInput += "\n"
    
    inputs = fromAscii(textInput)
    
    inputDeque, cmd, pc, base = inputs, commands, 0, 0
    while(True):
        term, output, newCmd, newPc, newBase = IntCode.run(inputDeque, cmd, pc, base)
        if(interactive):
            print(toAscii(output))
        if(term == 0):
            print(toAscii(output).split("\n")[-2].split(" ")[-8])
            break
        
        inputDeque = input("Requesting input: ")
        if(inputDeque == "q"):
            break
        else:
            inputDeque = fromAscii(inputDeque)
            inputDeque.append(10)
            cmd = newCmd
            pc = newPc
            base = newBase
            