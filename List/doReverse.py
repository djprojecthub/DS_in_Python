def doReverse(l):
    s = 0
    e = len(l) - 1

    while s < e:
        tmp = l[s]
        l[s] = l[e]
        l[e] = tmp
        s = s + 1
        e = e - 1

    return l


print(doReverse([10, 40, 30, 20, 50]))
