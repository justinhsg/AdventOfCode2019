from utils import fractions
from collections import deque
import math
def main(path):
    with open(path) as infile:
        lines = infile.read().split('\n')
    
    
    asteroids = []
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if(lines[y][x] == '#'):
                asteroids.append((x,y))
    
    maxSeen = 0
    bestPos = (-1, -1)
    for (x,y) in asteroids:
        grads = set()
        for(x2, y2) in asteroids:
            if(x == x2 and y == y2):
                continue
            grads.add( fractions.simplify((x2-x, y2-y)))
        if(len(grads) > maxSeen):
            maxSeen = len(grads)
            bestPos = (x,y)
    print(maxSeen)
    c = 0
    angled = dict()
    angles = []
    for(x2, y2) in asteroids:
        if(bestPos[0] == x2 and bestPos[1] == y2):
            continue
        grad = fractions.simplify((y2-bestPos[1], x2-bestPos[0]))
        angle = math.atan2(*grad)+math.pi*0.5
        if(angle < 0):
            angle += 2*math.pi
        if(angle not in angled):
            angled[angle] = []
            angles.append(angle)
            c += 1
        angled[angle].append((x2, y2))
    angles = sorted(angles)
    
    def distFromBest(a):
        return fractions.dist(bestPos, a)
    
    for angle in angles:
        angled[angle] = deque(sorted(angled[angle], key=distFromBest))
    asteroidOrder = []
    
    
    
    while(len(asteroidOrder) < len(asteroids)-1):
        for angle in angles:
            if(len(angled[angle])!=0):
                asteroidOrder.append(angled[angle].popleft())
            
    print(asteroidOrder[199][0]*100+asteroidOrder[199][1])
    
            
#312
   