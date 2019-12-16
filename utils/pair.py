def tuple_add(a,b):
    return tuple(a[i] + b[i] for i in range(len(a)))
def list_add(a,b):
    return list(a[i] + b[i] for i in range(len(a)))

def abs_sum(a):
    return sum(map(abs, a))
    
def prod(a):
    tot = 1
    for x in a:
        tot *= x
    return tot