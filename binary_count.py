def checkio(number):
    return str(bin(number)).count('1')

# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    print(checkio(5))
