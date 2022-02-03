def min(*args, **kwargs):
    key = kwargs.get("key", None)

    minnum = 0

    for x in args:
        if x < minnum:
            minnum = x

    return minnum


def max(*args, **kwargs):
    key = kwargs.get("key", None)

    print(args)
    return None

if __name__ == '__main__':
        #These "asserts" using only for self-checking and not necessary for auto-testing
    print max(3, 2) == 3, "Simple case max"
    print min(3, 2) == 2, "Simple case min"
    print max([1, 2, 0, 3, 4]) == 4, "From a list"
    print min("hello") == "e", "From string"
    print max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    print min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"