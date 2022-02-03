def checkio(number):
    listnum = list(str(number))

    multi = 1
    for strnum in listnum:
        if(int(strnum) != 0):
            multi = multi * int(strnum)

    return multi

if __name__ == '__main__':
    print(checkio(12305))
