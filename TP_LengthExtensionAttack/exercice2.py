from itertools import cycle
from hashlib import md5
import os

from utils import listener


# DO NOT CHANGE THOSE THREE LINES
FLAG_END = os.urandom(52)
FLAG = b'm1cryptoo' + FLAG_END #très important de garder de coté que ça commence par m1cryptoo
print(FLAG)


def bxor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


class Challenge():
    def __init__(self):
        self.before_input = "Enter data\n"

    def challenge(self, msg):
        if "option" not in msg:
            return {"error": "You must send an option to this server."}

        elif msg["option"] == "message":
            data = bytes.fromhex(msg["data"])
            if len(data) < len(FLAG):
              return {"error": "Bad input"}

            salted = bxor(data, cycle(FLAG))
            return {"hash": md5(salted).hexdigest()}

        else:
            return {"error": "Invalid option"}


import builtins; builtins.Challenge = Challenge # hack to enable challenge to be run locally, see https://cryptohack.org/faq/#listener
"""
When you connect, the 'challenge' function will be called on your JSON
input.
"""
listener.start_server(port=13407)
