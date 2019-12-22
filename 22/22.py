import re
def main(path):
    with open(path, "r") as infile:
        lines = infile.read().split("\n")
    
    commands = tuple(map(lambda x: (x.split(" ")), lines))
    
    
    #Evaluates x^e mod m 
    #Use pow(x,e,m) in Python
    def modPow(x, e, m):
        y = x
        ans = 1
        while(e > 0):
            if(e%2 == 1):
                ans = (ans*y)% m
            e //= 2
            y = (y*y)%m
        return ans
    
    
    #Gets the inverse y so that x*y = 1 mod(prime)
    #Exploits Fermat's Little Theorem
    def modInverse(x, prime):
        return modPow(x%prime, prime-2, prime)
    
    #Gets the card number at a given index
    def getNumber(deck, idx, size):
        fst, inc = deck
        return (fst+inc*idx) % size
    
    #Gets the index for a given card number
    def getIdx(deck, number, size):
        fst, inc = deck
        return ((number-fst)*modInverse(inc, size))%size
    
    #Performs one shuffle on a given deck
    def shuffle(deck, size):
        for command in commands:
            fst, inc = deck
            if(command[0] == "cut"):
                val = int(command[-1])
                deck = ((fst+inc*val)%size, inc)
            elif(command[0] == "deal"):
                if(command[1] == "into"):
                    deck = ((fst-inc)%size, -inc)
                elif(command[1] == "with"):
                    val = int(command[-1])
                    deck = (fst, (inc*modInverse(val, size)) % size)
        return deck
        
        
    DECKSIZE = 10007
    deck = shuffle((0,1), DECKSIZE)
    print(getIdx(deck, 2019, DECKSIZE))
    
    #Maths can be explained here:
    #https://www.reddit.com/r/adventofcode/comments/ee0rqi/2019_day_22_solutions/fbnkaju/
    
    #Performs n shuffles starting from an ordered deck of cards
    def shufflen(iterations, size):
        dFst, mInc = shuffle((0,1), size)
        newInc = modPow(mInc, iterations, size)
        newFst = (dFst * (1-newInc) * modInverse(1-mInc, size))%size
        return (newFst, newInc)
    
    DECKSIZE = 119315717514047
    ITERATIONS = 101741582076661
    deck2 = shufflen(ITERATIONS, DECKSIZE)
    fst, inc = deck2
    print(getNumber(deck2, 2020, DECKSIZE))