from collections import deque
def main(path):
    with open(path) as infile:
        line = infile.read()
    
    WIDTH = 25
    HEIGHT = 6
    
    #WIDTH = 3
    #HEIGHT = 2
    
    AREA = WIDTH*HEIGHT
    layers = []
    for i in range(len(line)//AREA):
        layers.append(line[AREA*i: AREA*(i+1)])
    minZeroes = AREA+1
    part1 = 0
    for layer in layers:
        nZeroes = layer.count('0')
        if(nZeroes < minZeroes):
            minZeroes = nZeroes
            part1 = layer.count('1')*layer.count('2')
    print(part1)
    
    for i in range(HEIGHT):
        output = ''
        for j in range(WIDTH):
            pixelIdx = j+i*WIDTH
            for layer in layers:
                if(layer[pixelIdx] == '2'):
                    continue
                else:
                    output = output + (' ' if layer[pixelIdx]=='0' else '#')
                    break
        print(output)
        
        