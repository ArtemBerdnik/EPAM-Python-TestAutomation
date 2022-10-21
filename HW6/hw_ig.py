from collections.abc import Iterator
from collections.abc import Iterable

# 1. Implement a function that flatten incoming data (non-iterables and elements from iterables)
# and returns an iterator

# # example input
# a = [1, 2, 3]
# b = 6
# c = 'zhaba'
# d = [[1, 2], [3, 4]]
#
# for _ in merge_elems(a, b, c, d):
#     print(_, end=' ')

# output: 1 2 3 6 z h a b a 1 2 3 4


def merge_elems(*elems) -> Iterator:
    for element in elems:
        if isinstance(element, Iterable):
            for obj_ in element:
                if isinstance(obj_, str):
                    for char in obj_:
                        yield char
                elif isinstance(obj_, Iterable) and not isinstance(obj_, str):
                    yield from merge_elems(obj_)
                else:
                    yield obj_
        else:
            yield element


# 2. Implement a map-like function that returns an iterator 
# (extra functionality: if arg function can't be applied, return element as is + text exception)
#
# def map_like(fun, *elems):
#     pass
#
# # example input
# a = [1, 2, 3]
# b = 6
# c = 'zhaba'
# d = True
# fun = lambda x: x[0]
#
# for _ in map_like(fun, a, b, c, d):
#     print(_)

# output:
# 1
# 6: 'int' object is not subscriptable
# z
# True: 'bool' object is not subscriptable

def map_like(fun, *elems) -> Iterator:
    for element in elems:
        try:
            yield fun(element)
        except TypeError as e:
            yield f"{element}: {str(e)}"
