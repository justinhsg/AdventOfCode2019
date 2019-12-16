#Need Dict
#Excess Dict

#Dict maps Result -> (qty, [(qty, req),...])
import math
def main(path):
    with open(path) as infile:
        lines = infile.read().split('\n')
    
    recipes = dict()
    
    for line in lines:
        (bef, aft) = line.split(" => ")
        aftQty, aftType = aft.split(" ")
        befs = bef.split(", ")
        ins = []
        for recipePair in befs:
            (qty, type) = recipePair.split(" ")
            inPair = (int(qty), type)
            ins.append(inPair)
        recipes[aftType] = (int(aftQty), ins)
    
    
    needs = dict()

    needs['FUEL'] = 0
    nOre = 0
    nFuel = 0
    
    qtys = []
    excesses = []
    
    def getOre(nFuel):
        needs = dict()
        needs['FUEL'] = nFuel
        excess = dict()
        for output in recipes:
            excess[output] = 0
        nOre = 0
        while(len(needs)!=0):
            item = list(needs)[0]
            
            itemQty = needs[item]
            #print("I need {} {}".format(itemQty, item))
            (recipeQty, recipeNeeds) = recipes[item]
            #print("Using Recipe {} => {} {}".format(recipeNeeds, recipeQty, item))
            nTimes = math.ceil(itemQty/recipeQty)
            #print("Recipe needs to be used {} times".format(nTimes))
            
            
            for (needQty, needItem) in recipeNeeds:
                amountNeeded = nTimes*needQty
                if(needItem == 'ORE'):
                    nOre += amountNeeded
                    continue
                if(needItem in excess):
                    excessQty = excess[needItem]
                    if(amountNeeded > excessQty):
                        excess[needItem] = 0
                        amountNeeded -= excessQty
                    else:
                        excess[needItem]-=amountNeeded
                        amountNeeded = 0
                if(amountNeeded!=0):
                    if(needItem not in needs):
                        needs[needItem] = 0
                    needs[needItem]+=amountNeeded
            excessAmt = (nTimes*recipeQty - itemQty)
            excess[item]+= excessAmt
            needs.pop(item, None)
        return nOre
    
    print(getOre(1))
    fuelNeeded = 1
    while(True):
        nOre = getOre(fuelNeeded)
        if(nOre >= 1e12):
            break
        else:
            fuelNeeded *= 2
    
    (ub) = fuelNeeded
    (lb) = fuelNeeded//2
    while(ub-lb > 1):
        newMidpt = (ub+lb) //2
        nOre = getOre(newMidpt)
        if(nOre < 1e12):
            lb = newMidpt
        elif(nOre > 1e12):
            ub = newMidpt
    print(lb)
        
        
        