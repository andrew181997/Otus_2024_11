import requests
import pytest
import pprint
BASE_URL = "https://api.openbrewerydb.org/v1/breweries/"

def single_brawery():
    result = requests.get(BASE_URL+'b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0')
    return result.json(), result.status_code

def list_braweries():
    params ={'per_page': 3}
    result = requests.get(BASE_URL, params=params)
    return result.json(), result.status_code

def  breweries_in_california():
        params ={'per_page': 3, 'by_state': 'california'}
        result = requests.get(BASE_URL, params=params)
        return result.json(), result.status_code

def sort_for_type():
        params ={'per_page': 3, 'by_state': 'california', 'sort':'type,name:asc'}
        result = requests.get(BASE_URL, params=params)
        return result.json(), result.status_code

def count_braweries():
        params ={'size': 6}
        result = requests.get(BASE_URL+'random', params=params)
        return result.json(), result.status_code



def test_single_brawery():
    json_data, status_code = single_brawery()
    # Проверка, что статус-код равен 200 (успешный запрос)
    assert status_code == 200, f"Expected 200, but got {status_code}"
    # Проверка, что ответ в JSON имеет ожидаемые ключи
    assert "name" in json_data, "Expected 'name' key in JSON response"

def test_list_braweries():
    json_data, status_code = list_braweries() #
    # Проверка, что статус-код равен 200 (успешный запрос)
    assert status_code == 200, f"Expected 200, but got {status_code}"
    # Проверка, что ответ в JSON имеет ожидаемые ключ
    assert json_data[0].get('brewery_type') == "micro"
@pytest.mark.parametrize("city, num_item", [("San Diego", 0), ("Petaluma", 1), ("Westlake Village", 2)])
def  test_by_state(city, num_item):
    json_data, status_code = breweries_in_california()
    # Проверка, что статус-код равен 200 (успешный запрос)
    assert status_code == 200, f"Expected 200, but got {status_code}"
    # Проверка, что ответ в JSON имеет ожидаемые ключ
    assert json_data[num_item].get('city') == city

@pytest.mark.parametrize("phone, num_item", [("4153690900", 0), ("4152330857", 1), ("6508678476", 2)])
def  test_correct_phone(phone, num_item):
    json_data, status_code = sort_for_type()
    # Проверка, что статус-код равен 200 (успешный запрос)
    assert status_code == 200, f"Expected 200, but got {status_code}"
    # Проверка, что ответ в JSON имеет ожидаемые ключ
    assert json_data[num_item].get('phone') == phone


def  test_count_braweries():
    json_data, status_code = count_braweries()
    # Проверка, что статус-код равен 200 (успешный запрос)
    assert status_code == 200, f"Expected 200, but got {status_code}"
    # Проверка, что количество элементов словаря равно 6 как в методе.
    assert len(json_data) == 6