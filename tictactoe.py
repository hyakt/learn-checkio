def checkio(game_result):
    for x in range(len(game_result)):
        for y in range(len(game_result[x])):
            if game_result[x][0] == game_result[x][1] == game_result[x][2]:
                return game_result[x][0]
            elif game_result[0][y] == game_result[1][y] == game_result[2][y]:
                return game_result[0][y]
            elif game_result[0][0] == game_result[1][1] == game_result[2][2]:
                return game_result[0][0]
            elif game_result[0][2] == game_result[1][1] == game_result[2][0]:
                return game_result[0][2]
            elif "." not in game_result[x]:
                return "D"
            else:
                pass

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print checkio([
        "X.O",
        "XX.",
        "XOO"])
    # assert checkio([
    #     "X.O",
    #     "XX.",
    #     "XOO"]) == "X", "Xs wins"
    # assert checkio([
    #     "OO.",
    #     "XOX",
    #     "XOX"]) == "O", "Os wins"
    # assert checkio([
    #     "OOX",
    #     "XXO",
    #     "OXX"]) == "D", "Draw"
    # assert checkio([
    #     "O.X",
    #     "XX.",
    #     "XOO"]) == "X", "Xs wins again"

