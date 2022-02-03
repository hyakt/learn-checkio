# coding:utf-8
def check_connection(network, first, second):
    # TODO:それぞれの関係性のあるものをリストで連結
    results = []

    for dr in network:
        drone1, drone2 = dr.split("-")
        if len(results) == 0:
            results.append(set([drone1, drone2]))
            continue

        for res in results:
            if drone1 in res:
                res.add(drone2)
                break
            elif drone2 in res:
                res.add(drone1)
                break
        else:
            results.append(set([drone1, drone2]))

    for dr in network:
        drone1, drone2 = dr.split("-")
        if len(results) == 0:
            results.append(set([drone1, drone2]))
            continue

        for res in results:
            if drone1 in res:
                res.add(drone2)
                break
            elif drone2 in res:
                res.add(drone1)
                break
        else:
            results.append(set([drone1, drone2]))

    print(results)

    # TODO:firstとsecondをリスト内？から検索してくる
    for res in results:
        if (first in res) and (second in res):
            return True
    else:
        return False

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing

    # print(check_connection(
    #     ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
    #      "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    #     "scout2", "scout3"))

    print(check_connection(("nikola-robin", "batman-nwing", "mr99-batman",
                            "mr99-robin", "dr101-out00", "out00-nwing",), "dr101", "mr99"))

    # assert check_connection(
    #     ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
    #      "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    #     "scout2", "scout3") == True, "Scout Brotherhood"
    # assert check_connection(
    #     ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2", "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"), "super", "scout2") == True, "Super Scout"
    # assert check_connection(
    #     ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2", "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"), "dr101", "sscout") == False, "I don't know any scouts."
