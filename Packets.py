import json


class TestPacket:


    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def encode(self):
        return ("{\"test\": " +
                "{\"a\": " + str(self.a)
                + ",\"b\": " + str(self.b)
                + ",\"c\": " + str(self.c) + "}}").encode("utf-8")

