import math

def period(L, g):
    return T = 2 * math.pi * (math.sqrt(L/g))
    try:
        if g == 0:
            raise ValueError
    except TypeError:
        raise TypeError
    except NameError:
        raise NameError