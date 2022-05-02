# USING BITWISE OPERATOR
def findOdd(l):
    res = 0
    for x in l:
        res = res ^ x
    return res


# SIMPLE METHOD
def OnlyOdd(l):
    for x in l:
        if l.count(x) % 2 != 0:
            return x


print(OnlyOdd([10, 10, 20, 20, 30, 40, 40]))
print(findOdd([10, 20, 20, 30, 10]))
