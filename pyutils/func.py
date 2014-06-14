# coding: utf-8
import functools

def curry(fn, argc=None):
    """A decorator curries the given function.

    >>> @curry
    ... def foo(a, b, c):
    ...     return (a, b, c)
    ...
    >>> foo(1)(2)(3)
    (1, 2, 3)
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
