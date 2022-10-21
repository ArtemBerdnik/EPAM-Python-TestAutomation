import pytest
from hw_task2 import TableData


@pytest.fixture
def get_db_details():
    database_name = 'HW5/task2/example.sqlite'
    table_name = 'presidents'
    return (
        database_name,
        table_name
    )


@pytest.fixture
def get_db_details_with_updates():
    database_name = 'HW5/task2/example.sqlite'
    table_name = 'presidents'
    president_name = 'Test_President'
    president_age = 18
    president_country = 'Mongolia'
    return (
        database_name,
        table_name,
        president_name,
        president_age,
        president_country
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


def test_updates_in_db(get_db_details_with_updates):
    (
        database_name,
        table_name,
        president_name,
        president_age,
        president_country
    ) = get_db_details_with_updates

    presidents = TableData(database_name, table_name)

    amount_of_entries_in_db = len(presidents)

    TableData.update_data_in_table(president_name, president_age, president_country)

    assert len(presidents) == amount_of_entries_in_db + 1
    assert president_name in presidents

    TableData.delete_data_in_table("presidents", "name", president_name)
