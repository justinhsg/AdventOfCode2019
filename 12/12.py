from utils import pair, fractions
import re
def main(path):
    with open(path) as infile:
        lines = infile.read().split('\n')
        
    def toTriplet(line):
        rawsplit = re.split('=|,|>', line)
        return list(map(int, (rawsplit[1], rawsplit[3], rawsplit[5])))
        
    pos = list(map(toTriplet, lines))
    vel = list([0,0,0] for _ in range(4))
    
    t = 0
    while(t != 1000):
        t+=1
        for dim in range(3):
            for curMoon in range(4):
                for othMoon in range(4):
                    if(pos[curMoon][dim] > pos[othMoon][dim]):
                        vel[curMoon][dim]-=1
                    elif(pos[curMoon][dim] < pos[othMoon][dim]):
                        vel[curMoon][dim]+=1
        
        for moon in range(4):
            pos[moon] = pair.list_add(pos[moon], vel[moon])
    totalEnergy = 0    
    for moon in range(4):
        totalEnergy += pair.abs_sum(pos[moon]) * pair.abs_sum(vel[moon])
    print(totalEnergy)
    
    
    pos = list(map(toTriplet, lines))
    vel = list([0,0,0] for _ in range(4))
    cycles = [0 for i in range(3)]
    for dim in range(3):
        t = 0
        initp = [pos[i][dim] for i in range(4)]
        p = [pos[i][dim] for i in range(4)]
        initv = [0 for _ in range(4)]
        v = [0 for _ in range(4)]
        while(True):
            t+=1
            for moon in range(4):
                for othMoon in range(4):

                    if (p[moon] > p[othMoon]):
                        v[moon] -= 1
                        
                    elif(p[moon] < p[othMoon]):
                        v[moon] += 1
                        
                        
            for moon in range(4):
                p[moon] += v[moon]
                
            if(p == initp and v == initv):
    
                cycles[dim] = t
                break;
                
    
    print(fractions.lcm(fractions.lcm(cycles[0], cycles[1]), cycles[2]))
    
    