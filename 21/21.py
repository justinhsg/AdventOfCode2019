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
#J = !(A*B*C)*D
#Jump if (A or B or C has a hole) and (D is solid)
#Jump if there is a hole and the robot can land after jumping
    part1 =\
"OR A J\n\
AND B J\n\
AND C J\n\
NOT J J\n\
AND D J\n\
WALK\n"
#J = !(A&B&C)&D&(E|H)
#Jump if (A or B or C has a hole) and (D is solid) and (E is solid or H is solid)
#Jump if there is a hole, robot can land after jumping, and if robot can either walk or jump again afterward.
    part2 =\
"OR A J\n\
AND B J\n\
AND C J\n\
NOT J J\n\
AND D J\n\
OR H T\n\
OR E T\n\
AND T J\n\
RUN\n"

    print(runIntCode(fromAscii(part1))[-1])
    print(runIntCode(fromAscii(part2))[-1])