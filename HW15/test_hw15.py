import pytest
import requests

url = "https://api.punkapi.com/v2/beers/8"


@pytest.mark.parametrize("attributes, expected_values", [(['name', 'abv'], ['Fake Lager', 4.7])])
def test_get(attributes: tuple, expected_values: tuple):
    r = requests.get(url)
    assert r.status_code == 200
    assert r.json()[0][attributes[0]] == expected_values[0]
    assert r.json()[0][attributes[1]] == expected_values[1]


def test_delete():
    r = requests.delete(url)
    assert r.status_code == 404
    assert r.json()['message'] == "No endpoint found that matches '/v2/beers/8'"
