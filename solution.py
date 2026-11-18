import functools

def solve(value):
    return functools.reduce(lambda total, c: total * value["x"] + c, value["coefficients"], 0)
