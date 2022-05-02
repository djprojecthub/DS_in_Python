def getSecMax(l):
    if len(l) <= 1:
        return None
    lar = l[0]
    slar = None

    for x in l[1:]:
        if x > lar:
            slar = lar
            lar = x
        # ignore x == lar comparison
        elif x != lar:
            if slar is None or slar < x:
                slar = x

    return slar


print(getSecMax([10, 15, 11, 5, 20, 30]))
print(getSecMax([45, 45, 30]))
