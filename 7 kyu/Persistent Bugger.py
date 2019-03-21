def persistence(n):
    # I think turning it into a string would be
    # more efficient than dividing by 10 repeatedly for large numbers
    count = 0;
    while n >= 10:
        temp = str(n)
        tempval = 1;
        for char in temp:
            tempval *= int(char)
        count += 1
        n = tempval
    return count