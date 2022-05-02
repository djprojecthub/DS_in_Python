def smallerElements(l, x):
    smallerList = []
    i = 0
    while l[i] < x:
        smallerList.append(l[i])
        i = i + 1
    return smallerList


if __name__ == "__main__":
    input_list = [int(item) for item in input("Enter list items: ").split()]
    smallerThan = int(input("Enter smaller than number: "))
    print(smallerElements(input_list, smallerThan))
