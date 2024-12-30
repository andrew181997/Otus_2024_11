import requests
import pytest
BASE_URL = 'https://dog.ceo/api'
ALL_URL = '/breeds/list/all'
RANDOM_IMAGE = '/breeds/image/random'
RANDOM_3 = 'https://dog.ceo/api/breeds/image/random/'



def test_get_all_dogs():
    r = requests.get(BASE_URL+ALL_URL)
    assert r.ok == True

@pytest.mark.parametrize("num,expected_status", [
    ('3', 200),
    ('5', 200),
    ('50',200),
])
def test_get_count_photo(num, expected_status):
    r = requests.get(BASE_URL+RANDOM_IMAGE+num)
    assert r.status_code == expected_status

@pytest.mark.parametrize("breed ,expected_status", [
    ('pug', 200),
    ('hound', 200),
    ('wewe', 404),
    ({"dda"}, 400)
])
def test_get_photo_breed(breed, expected_status):
    r = requests.get(f"{BASE_URL}/breed/{breed}/images")
    assert r.status_code == expected_status



@pytest.mark.parametrize("breed, expected_status", [
    ("affenpinscher", 200),
    ("beagle", 200),
    ("boxer", 200),
    ("404", 404)
])
def test_get_bread(breed,expected_status):
    r = requests.get(BASE_URL+'/breed/'+ breed +'/images/random')
    assert r.status_code == expected_status