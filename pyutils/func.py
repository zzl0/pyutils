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


class memo(object):
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    '''
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
       if not isinstance(args, collections.Hashable):
           # uncacheable. a list, for instance.
           # better to not cache than blow up.
           return self.func(*args)
       if args in self.cache:
           return self.cache[args]
       else:
           value = self.func(*args)
           self.cache[args] = value
           return value

    def __repr__(self):
       '''Return the function's docstring.'''
       return self.func.__doc__

    def __get__(self, obj, objtype):
       '''Support instance methods.'''
       return functools.partial(self.__call__, obj)