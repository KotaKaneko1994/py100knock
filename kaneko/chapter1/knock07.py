# -*- encoding: utf-8 -*-
def makeString(x, y, z):
    return u"%s時の%sは%s" % (x, y, z)

if __name__ == "__main__":
    print(makeString(12, "気温", 22.4))