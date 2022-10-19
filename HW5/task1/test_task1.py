import pytest
from hw_task1 import KeyValueStorage


@pytest.mark.parametrize("data_", ["task1.txt"])
def test_positional_only(data_):
    test = KeyValueStorage(data_)
    assert test.name == 'kek'
    assert test['name'] == 'kek'
    assert test.power == 9001
    assert test['power'] == 9001


@pytest.mark.parametrize("data_", ["task1_negative.txt"])
def test_positional_only(data_):
    with pytest.raises(ValueError) as err:
        _ = KeyValueStorage(data_)
    assert "int value can not be a key in dict" in str(err.value)
