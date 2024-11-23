def area(a, b, c):
    assert all(side >= 0 for side in (a, b, c))
    assert a + b > c and a + c > b and b + c > a
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def perimeter(a, b, c):
    assert all(side >= 0 for side in (a, b, c))
    assert a + b > c and a + c > b and b + c > a
    return a + b + c
