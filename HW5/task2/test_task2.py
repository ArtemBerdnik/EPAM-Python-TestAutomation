import pytest
from hw_task2 import TableData


@pytest.fixture
def get_db_details():
    database_name = 'example.sqlite'
    table_name = 'presidents'
    return (
        database_name,
        table_name
    )


def test_presidents(get_db_details):
    (
        database_name,
        table_name
    ) = get_db_details
    presidents = TableData(database_name, table_name)

    assert len(presidents) == 3
    assert presidents['Yeltsin'] == ('Yeltsin', 999, 'Russia')
    assert 'Trump' in presidents
    for president in presidents:
        assert president['name'] is not None and president['name'] in ['Big Man Tyrone', 'Trump', 'Yeltsin']
