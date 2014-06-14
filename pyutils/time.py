import time


def timer(fn, *args):
    "Time the application of fn to args. Return (result, seconds)."
    start = time.clock()
    return fn(*args), time.clock() - start
