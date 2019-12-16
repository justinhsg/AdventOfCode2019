from collections import deque

def main(path):
    with open(path) as infile:
        lines = infile.read().split('\n')
        
    orbits = list(map(lambda x: tuple(x.split(')')), lines))
    
    orbitDict = dict()
    adjDict = dict()
    
    for(parent, child) in orbits:
        if(parent not in orbitDict):
            orbitDict[parent] = []
        if(child not in orbitDict):
            orbitDict[child] = []
        if(parent not in adjDict):
            adjDict[parent] = []
        if(child not in adjDict):
            adjDict[child] = []
        orbitDict[parent].append(child)
        adjDict[parent].append(child)
        adjDict[child].append(parent)
    
    
    nOrbits = 0
    bfsQueue = deque()
    bfsQueue.append(('COM', 0))
    while(len(bfsQueue) != 0):
        (curPlanet, curOrbits) = bfsQueue.popleft()
        nOrbits += curOrbits
        for child in orbitDict[curPlanet]:
            bfsQueue.append((child, curOrbits+1))
    print(nOrbits)
    
    
    searchQueue = deque()
    visited = {'YOU'}
    searchQueue.append(('YOU', 0))
    while(len(searchQueue) != 0):
        (curPlanet, curOrbits) = searchQueue.popleft()
        if(curPlanet == 'SAN'):
            print(curOrbits - 2)
            break
        for child in adjDict[curPlanet]:
            if(child not in visited):
                visited.add(child)
                searchQueue.append((child, curOrbits+1))
                