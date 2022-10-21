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
    results = []

    def merge_sub_elements(sub_element):
        if isinstance(sub_element, Iterable):
            for obj_ in sub_element:
                if isinstance(obj_, str):
                    results.extend(sub_element)
                    break
                if isinstance(obj_, Iterable) and not isinstance(obj_, str):
                    merge_sub_elements(obj_)
                else:
                    results.extend(sub_element)
                    break
        else:
            results.append(sub_element)

    for element in elems:
        merge_sub_elements(element)
    yield results


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
    result = []
    for element in elems:
        try:
            result.append(fun(element))
        except TypeError as e:
            result.append(f"{element}: {str(e)}")
    yield result
