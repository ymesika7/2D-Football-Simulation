# Convert string type "(x, y)"(=tuple) to int(x) and int(y)


def getX(tupleToInt):
    x = tupleToInt[tupleToInt.index('(') + 1:tupleToInt.index(',')]
    return int(x)


def getY(tupleToInt):
    y = tupleToInt[tupleToInt.index(',') + 2:tupleToInt.index(')')]
    return int(y)
