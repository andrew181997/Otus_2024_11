import requests
import pytest


BASE_URL = 'https://jsonplaceholder.typicode.com'

def get_posts():
    result = requests.get(BASE_URL+'/posts')
    return result.json(), result.status_code

def get_comments():
    result = requests.get(BASE_URL+'/comments')
    return result.json(), result.status_code

def get_albums():
    result = requests.get(BASE_URL+'/albums')
    return result.json(), result.status_code

def get_todos():
    result = requests.get(BASE_URL+'/todos')
    return result.json(), result.status_code

def get_users():
    result = requests.get(BASE_URL+'/users')
    return result.json(), result.status_code

@pytest.mark.parametrize("key, num_dict", [("body", 0), ("title", 1), ("id", 2)])
def test_posts(key,num_dict):
    json_data, status_code = get_posts()
    # Проверка, что статус-код равен 200 (успешный запрос)
    assert status_code == 200, f"Expected 200, but got {status_code}"
    # Проверка, что ответ в JSON имеет ожидаемые ключи
    assert key in json_data[num_dict], "Expected 'id' key in JSON response"

@pytest.mark.parametrize("email, num_item", [("Eliseo@gardner.biz", 0), ("Jayne_Kuhic@sydney.com", 1), ("Nikita@garfield.biz", 2)])
def test_comments(email, num_item):
    json_data, status_code = get_comments()
    # Проверка, что статус-код равен 200 (успешный запрос)
    assert status_code == 200, f"Expected 200, but got {status_code}"
    # Проверка, что ответe значения по ключу email совпадают с ожидаемыми
    assert json_data[num_item].get('email') == email

def test_albums():
    json_data, status_code = get_albums()
    assert status_code == 200, f"Expected 200, but got {status_code}"
    assert len(json_data) == 100

def test_todos():
    json_data, status_code = get_todos()
    assert status_code == 200, f"Expected 200, but got {status_code}"

def test_users():
    json_data, status_code = get_users()
    assert status_code == 200, f"Expected 200, but got {status_code}"