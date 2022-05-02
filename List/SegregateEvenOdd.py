def SegregateEvenOdd(l):
    even_list = []
    odd_list = []
    
    for i in l:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    return even_list, odd_list


if __name__ == "__main__":
    input_list = [10, 41, 30, 15, 80]
    even_list, odd_list = SegregateEvenOdd(input_list)

    print(even_list)
    print(odd_list)
