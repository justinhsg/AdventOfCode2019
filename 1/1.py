def main(path):
    with open(path) as infile:
        lines = str(infile.read()).split("\n")
        
    masses = list(map(lambda x: int(x), lines))

    part1 = 0
    part2 = 0
    for mass in masses:
        fuel = mass//3 - 2
        part1+= fuel
        while(fuel > 0):
            part2+=fuel
            fuel = fuel//3-2
    print(part1)
    print(part2)
