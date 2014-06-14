# coding: utf-8

def group(lst, n):
    """ Return a new list in which the elements of `lst` are grouped into
    sublists of length `n`.

    >>> list(group(range(4), 2))
    [[0, 1], [2, 3]]
    >>> list(group(range(5), 2))
    [[0, 1], [2, 3], [4]]
    """
    assert n > 0, 'n must > 0'
    for i in range(0, len(lst), n):
        yield lst[i: i+n]


def most(score_fn, lst):
    """ Return the element with the highest score.

    >>> most(len, ["12", "123", "456"])
    ('123', 3)
    """
    if not lst:
        return None, None
    wins = lst[0]
    max = score_fn(wins)
    for obj in lst[1:]:
        score = score_fn(obj)
        if score > max:
            wins = obj
            max = score
    return wins, max
