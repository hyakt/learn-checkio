def checkio(words):

    count = 0
    array = words.split(" ")

    for i, x in enumerate(array):
        if x.isalpha() is True:
            count += 1
        else:
            count = 0

        if count >= 3:
            return True

    return False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    checkio("hello world Hello")

Pass:
    checkio("one two 3 four 5 six 7 eight 9 ten eleven 12")
Fail:
    checkio("one two 3 four five six 7 eight 9 ten eleven 12")
