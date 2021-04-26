"""
yo sdofspod
sdf sdf

"""


class Employee:
    def __init__(self, fun):
        self.emp = []
        self.f = -1  # f, czyli najwieksza wartosc imprezy
        self.g = -1  # g, czyli najwieksza wartosc imprezy (ALE v nie idzie na nią)
        self.fun = fun


def f(v):
    if v.f >= 0: return v.f
    x = v.fun

    for u in v.emp:  # nasz v idzie więc, jego podwladni nie mogą pójść, liczymy ich g
        x += g(u)

    y = g(v)  # nasz v nie idzie, więc liczymy jego g(v)

    v.f = max(x, y)  # wybieram wartość większą
    return v.f


def g(v):
    if v.g >= 0: return v.g

    v.g = 0

    for u in v.emp:
        v.g += f(u)
    return v.g


if __name__ == '__main__':
    pass
