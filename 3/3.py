def main(path):
    with open(path) as infile:
        lines = infile.read().split('\n')
        
    wire1 = lines[0].split(',')
    wire2 = lines[1].split(',')
    
    points1 = [(0,0)]
    points2 = [(0,0)]
    
    def convertToPoints(wire, points):
        for inst in wire:
            dir = inst[0]
            dist = int(inst[1:])
            prevPoint = points[-1]
            if(dir == 'U'):
                points.append((prevPoint[0], prevPoint[1]-dist))
            elif(dir == 'D'):
                points.append((prevPoint[0], prevPoint[1]+dist))
            elif(dir == 'L'):
                points.append((prevPoint[0]-dist, prevPoint[1]))
            elif(dir == 'R'):
                points.append((prevPoint[0]+dist, prevPoint[1]))
                
    convertToPoints(wire1, points1)
    convertToPoints(wire2, points2)

    def sortPoints(pt1, pt2):
        if(pt1[0] == pt2[0]):
            if(pt1[1] < pt2[1]):
                return(pt1, pt2)
            else:
               return(pt2, pt1)
        else:
            if(pt1[0] < pt2[0]):
                return(pt1, pt2)
            else:
                return(pt2, pt1)
    minManhattan = 1e100
    minSteps = 1e100
    w1steps = 0
    for i in range(0, len(points1)-1):
        
        ((s1x, s1y), (e1x, e1y)) = sortPoints(points1[i], points1[i+1])
        #(s1x,s1y) = points1[i]
        #(e1x,e1y) = points1[i+1]
        w2steps = 0
        for j in range(0, len(points2)-1):
            
            ((s2x, s2y), (e2x, e2y)) = sortPoints(points2[j], points2[j+1])
            #print("Comparing ({}, {}) -> ({}, {}) and ({}, {}) -> ({}, {})".format(s1x, s1y, e1x, e1y, s2x, s2y, e2x, e2y))
            foundIntersection = False
            if(s1x == e1x):
                if(s2x == e2x):
                    if(s1x == s2x):
                        if(not(s1y > e2y and s2y > e1y)):
                            foundIntersection = True
                            (lb, rb) = (max(s1y, s2y), min(e1y, e2y))
                            if(lb <= 0 and rb >= 0):
                                intersection = (s1x, 0)
                            else:
                                intersection = (s1x, min(abs(lb), abs(rb)))
                else:
                    if(s1x >= s2x and s1x <= e2x):
                        if(s1y <= s2y and e1y >= s2y):
                            foundIntersection = True
                            intersection = (s1x, s2y)
                    
            else:
                if(s2y == e2y):
                    if(s1y == s2y):
                        if(not(s1x > e2x and s2x > e1x)):
                            foundIntersection = True
                            (lb, rb) =(max(s1x, s2x), min(e1x, e2x))
                            if(lb <= 0 and rb >= 0):
                                intersection = (0, s1y)
                            else:
                                intersection = (min(abs(lb), abs(rb)), s1y)
                else:
                    if(s1x <= s2x and e1x >= s2x):
                        if(s1y >= s2y and s1y <= e2y):
                            foundIntersection = True
                            intersection = (s2x, s1y)
            if(foundIntersection):
                dist = sum(map(abs, intersection))
                steps = w1steps + abs(intersection[0] - points1[i][0]) + abs(intersection[1] - points1[i][1]) + w2steps + abs(intersection[0] - points2[j][0]) + abs(intersection[1] - points2[j][1])
                if(dist != 0):
                    minManhattan = min(dist, minManhattan)
                if(steps != 0):
                    minSteps = min(steps, minSteps)
            w2steps += (e2x - s2x) + (e2y - s2y)
        w1steps += (e1x - s1x) + (e1y - s1y)
    print(minManhattan)
    print(minSteps)