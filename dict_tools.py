def invert(d):
    ou = dict()
    for x in d:
        ou[d[x]] = x
    return ou

def get_keys(d):
    ou = set()
    for x in d:
        ou.add(x)
    return ou

def get_values(d):
    ou = set()
    for x in d:
        ou.add(d[x])
    return x

def to_tuples(d):
    ou = []
    for x in d:
        ou.append((x,d[x]))
    return ou

def from_pairs(arr):
    ou = dict()
    for x in arr:
        ou[x[0]] = x[1]
    return ou

def from_parallel(k,v):
    ou = dict()
    for i in range(len(k)):
        ou[k] = v
    return ou

def lookup(d,q):
    ou = []
    for x in q:
        if x in d:
            ou.append(d[x])
        else:
            ou.append(None)
    return ou
