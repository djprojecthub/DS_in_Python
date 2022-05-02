def SegregateEvenOdd_listComp(l):

    even = [i for i in l if i % 2 == 0]
    odd = [j for j in l if j % 2 != 0]

    return even, odd


even, odd = SegregateEvenOdd_listComp([10, 20, 5, 13, 24])
print(even)
print(odd)
