def gcd(a, b):
    if(a < b):
        return gcd(b,a)
    if(b == 0):
        return a
    return gcd(b, a%b)

    
def lcm(a,b):
    return a * b // gcd(a,b)
def simplify(frac):
    (a,b) = frac
    if(a == 0):
        if(b==0):
            return frac
        else:
            return (0,b//abs(b))
    
    div = gcd(abs(a),abs(b))
    return(a//div, b//div)

    
def dist(a,b):
    return ((b[1] - a[1])**2 + (b[0] - b[1])**2)**0.5
    
def equiv(a,b):
    return simplify(a) == simplify(b)