import sys

def IntToBin(f, n):
    return "{:0>{}b}".format(n,f)

def HexToInt(h):
    return int(h)

def HexToBin(f, n):
    return IntToBin(int(f), HexToInt(n))