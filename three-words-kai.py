def checkio(words):

    array = words.split(" ")

    print([x for x in array])


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio("hello world Hello"))
