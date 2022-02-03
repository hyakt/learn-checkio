def checkio(data):
    # replace this for solutionn
    result = ""
    ones = ["", "I", "II", "III", "IV","V","VI","VII","VIII","IX"]
    tens = ["", "X", "XX", "XXX", "XL","L","LX","LXX","LXXX","XC"]
    hundreds = ["", "C", "CC", "CCC", "CD","D","DC","DCC","DCCC","CM"]
    thousands = ["", "M","MM","MMM"]

    mile = data//1000
    data = data - mile * 1000

    centum = data//100
    data = data - centum * 100

    decem = data//10
    data = data - decem * 10

    result = thousands[mile] + hundreds[centum] + tens[decem] + ones[data]
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio(1001))