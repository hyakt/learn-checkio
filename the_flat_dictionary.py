def flatten(dictionary):
    while dictionary:

if __name__ == '__main__':
    flatten({
        "name": {
            "first": "One",
            "last": "Drone"
        },
        "job": "scout",
        "recent": {},
        "additional": {
            "place": {
                "zone": "1",
                "cell": "2"}
        }
    })
