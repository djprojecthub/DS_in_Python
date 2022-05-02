# DON'T USE MAX() FUNCTION
def largest_in_list(l):
    if not l:
        return None
    max = l[0]
    for i in range(1, len(l)):
        if l[i] > max:
            max = l[i]

    return max


print(largest_in_list([30, 30, 20]))
