# coding: utf-8
import inspect

def curry(fn, argc=None):
    """A decorator curries the given function.
    """
    if argc is None:
        argc = fn.func_code.co_argcount

    @functools.wraps(fn)
    def p(*a):
        if len(a) == argc:
            return fn(*a)
        def q(*b):
            return fn(*(a+b))
        return curry(q, argc - len(a))
    return p
