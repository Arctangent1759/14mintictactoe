import requests
from sys import argv


def place_board(player, x, y):
    print requests.get("http://testbed.alexpchu.com/{}/{}/{}".format(player, x, y)).text

def clear():
    print requests.get("http://testbed.alexpchu.com/cb").text



if __name__ == "__main__":
    if argv[1] == "cb":
        clear()
    else:
        place_board(argv[1], argv[2], argv[3])