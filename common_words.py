def checkio(first, second):
    fl = first.split(',')
    sl = second.split(',')

    res = set()
    for f in fl:
        for s in sl:
            if f == s:
                res.add(s)

    res = list(res)
    res.sort()
    return ",".join(res)
# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    print(checkio("hello,world", "hello,earth"))
