from collections.abc import Generator

import pytest
from hw_ig import merge_elems, map_like


@pytest.mark.parametrize("a,b,c,d, expected", [(
        [1, 2, 3],
        6,
        'zhaba',
        [[1, 2], [3, 4]],
        [1, 2, 3, 6, 'z', 'h', 'a', 'b', 'a', 1, 2, 3, 4]
), (
        [[[1, 2], [3, 4]], [[5, 6], [7, 8]]],
        ['zhaba'],
        [['a', 'test']],
        [[1], [[3, 4]]],
        [1, 2, 3, 4, 5, 6, 7, 8, 'z', 'h', 'a', 'b', 'a', 'a', 't', 'e', 's', 't', 1, 3, 4]
)
]
                         )
def test_arguments_flattener(a, b, c, d, expected):
    assert isinstance(merge_elems(a, b, c, d), Generator)
    gen = merge_elems(a, b, c, d)
    for char in expected:
        assert next(gen) == char


@pytest.mark.parametrize("fun,a,b,c,d", [(
        lambda x: x[0],
        [1, 2, 3],
        6,
        'zhaba',
        True
)])
def test_map_like_flattener(fun, a, b, c, d):
    assert isinstance(map_like(fun, a, b, c, d), Generator)
    gen = map_like(fun, a, b, c, d)
    for char in [1, "6: 'int' object is not subscriptable", 'z', "True: 'bool' object is not subscriptable"]:
        assert next(gen) == char