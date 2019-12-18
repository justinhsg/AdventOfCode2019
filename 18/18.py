from collections import deque
import heapq
def main(path):
    with open(path) as infile:
        lines = infile.read().split('\n')
    
    grid = list(map(list, lines))
    
    doors = dict()
    keys = dict()
    start = None

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            char = grid[y][x]
            if(char.isalpha()):
                if(char.isupper()):
                    doors[char] = (x,y)
                else:
                    keys[char] = (x,y)
            elif(char == '@'):
                start = (x,y)
    
    keyNames = sorted(keys.keys())
    keyIntDict = dict()
    
    for i in range(len(keyNames)):
        keyIntDict[keyNames[i]] = 1<<i;
    
    nodes = ['@', *doors.keys(), *keys.keys()]
    nodesLoc = dict()
    nodesLoc['@'] = start
    for key in keys:
        nodesLoc[key] = keys[key]
    for door in doors:
        nodesLoc[door] = doors[door]
    
    nodeDist = dict()
    for node in nodes:
        nodeDist[node] = dict()
    
    visited = [[False for x in range(len(grid[y]))] for y in range(len(grid))]
    toExplore = deque();
    
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    
    def inRange(x,y):
        return x>=0 and x<len(grid[0]) and y>= 0 and y<len(grid)

    for node in nodes:
        visited = [[False for x in range(len(grid[y]))] for y in range(len(grid))]
        
        startPos = nodesLoc[node]
        toExplore.append((startPos, 0))
        visited[startPos[1]][startPos[0]] = True
        while(len(toExplore) != 0):
            curPos, curDis = toExplore.popleft()
            curX, curY = curPos
            gridChar = grid[curY][curX]
            if(gridChar in nodes and gridChar != node):
                nodeDist[node][gridChar] = curDis
            else:
                for i in range(4):
                    newX = curX + dx[i]
                    newY = curY + dy[i]
                    if(inRange(newX, newY)):
                        if(grid[newY][newX]!='#'):
                            if(not visited[newY][newX]):
                                visited[newY][newX] = True
                                toExplore.append(((newX, newY), curDis+1))

    bfDist = dict()
    for node in nodes:
        bfDist[node] = dict()
   
    pq = [(0, 0, '@')]
    heapq.heapify(pq)
    bfDist['@'][0] = 0
    
    def isSmaller(newDist, node, intKeyMap):
        if(intKeyMap not in bfDist[node]):
            return True
        else:
            return newDist < bfDist[node][intKeyMap] 
    fullKeys = (1<<len(keys))-1
    
    while(len(pq)!=0):
        curDist, curKeyMap, curNode = heapq.heappop(pq)
        if(curKeyMap == fullKeys):   
            print(curDist)
            break
        else:           
            for nextNode in nodeDist[curNode]:
                newDist = curDist + nodeDist[curNode][nextNode]
                nextKeyMap = curKeyMap
                if(nextNode.isupper()):
                    if(keyIntDict[nextNode.lower()] & nextKeyMap == 0):
                        #No key
                        continue
                elif(nextNode.islower()):
                    #Add key
                    nextKeyMap |= keyIntDict[nextNode]
                if(isSmaller(newDist, nextNode, nextKeyMap)):
                        bfDist[nextNode][nextKeyMap] = newDist
                        heapq.heappush(pq, (newDist, nextKeyMap, nextNode))
                
    

    #----------------------------------PART 2-----------------------------------------#
    
    
    grid2 = [ grid[y][:] for y in range(len(grid))]
    grid2[start[1]][start[0]] = '#'
    for i in range(4):
        grid2[start[1]+dy[i]][start[0]+dx[i]] = '#'
        
    grid2[start[1]-1][start[0]-1] = '@'
    grid2[start[1]-1][start[0]+1] = '$'
    grid2[start[1]+1][start[0]+1] = '%'
    grid2[start[1]+1][start[0]-1] = '&'
    
    newNodes = ['@', '$', '%', '&', *doors.keys(), *keys.keys()]
    
    nodesLoc = dict()
    nodesLoc['@'] = (start[0]-1, start[1]-1)
    nodesLoc['$'] = (start[0]+1, start[1]-1)
    nodesLoc['%'] = (start[0]+1, start[1]+1)
    nodesLoc['&'] = (start[0]-1, start[1]+1)
    
    for key in keys:
        nodesLoc[key] = keys[key]
    for door in doors:
        nodesLoc[door] = doors[door]
    
    
    newNodeDist = dict()
    for node in newNodes:
        newNodeDist[node] = dict()
    
    visited = [[False for x in range(len(grid2[y]))] for y in range(len(grid2))]
    toExplore = deque();
    
    for node in newNodes:
        visited = [[False for x in range(len(grid2[y]))] for y in range(len(grid2))]
        startPos = nodesLoc[node]
        toExplore.append((startPos, 0))
        visited[startPos[1]][startPos[0]] = True
        while(len(toExplore) != 0):
            curPos, curDis = toExplore.popleft()
            curX, curY = curPos
            gridChar = grid2[curY][curX]
            if(gridChar in newNodes and gridChar != node):
                newNodeDist[node][gridChar] = curDis
            else:
                for i in range(4):
                    newX = curX + dx[i]
                    newY = curY + dy[i]
                    if(inRange(newX, newY)):
                        if(grid2[newY][newX]!='#'):
                            if(not visited[newY][newX]):
                                visited[newY][newX] = True
                                toExplore.append(((newX, newY), curDis+1))
                 
    startNodes = "@$%&"        
    
    reachableKeys = dict()
    reachableVisited = set()
    for i in range(len(startNodes)):
        startNode = startNodes[i]
        reachableVisited.add(startNode)
        reachableKeys[startNode] = 0
        toExplore = deque([startNode])
        while(len(toExplore) != 0):
            curNode = toExplore.popleft()
            for nxtNode in newNodeDist[curNode]:
                if(nxtNode not in reachableVisited):
                    reachableVisited.add(nxtNode)
                    if(nxtNode.islower()):
                        reachableKeys[startNode]|=keyIntDict[nxtNode]
                    toExplore.append(nxtNode)
        
    
    bfDist = dict()
    pq = [(0, 0, startNodes)]
    heapq.heapify(pq)
    bfDist[startNodes] = dict()
    bfDist[startNodes][0] = 0

    def newIsSmaller(newDist, newNodes, intKeyMap):
        if(newNodes not in bfDist):
            bfDist[newNodes] = dict()
            return True
        elif(intKeyMap not in bfDist[newNodes]):
            return True
        else:
            return newDist < bfDist[newNodes][intKeyMap] 
    
    while(len(pq)!=0):
        curDist, curKeyMap, curNodes = heapq.heappop(pq)
        if(curKeyMap == fullKeys):   
            print(curDist)
            break
        else:
            for bot in range(4):
                if(reachableKeys[startNodes[bot]]&curKeyMap == reachableKeys[startNodes[bot]]):
                    continue
                curNode = curNodes[bot]
                for newNode in newNodeDist[curNode]:
                    newDist = curDist + newNodeDist[curNode][newNode]
                    newNodesList = list(curNodes)
                    newNodesList[bot] = newNode
                    newNodes = "".join(newNodesList)
                    newKeyMap = curKeyMap
                    if(newNode.isupper()):
                        if(keyIntDict[newNode.lower()]&curKeyMap == 0):
                            continue
                    elif(newNode.islower()):
                        newKeyMap |= keyIntDict[newNode]
                    if(newIsSmaller(newDist, newNodes, newKeyMap)):
                        bfDist[newNodes][newKeyMap] = newDist
                        heapq.heappush(pq, (newDist, newKeyMap, newNodes))
                    
    