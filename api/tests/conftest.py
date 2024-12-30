import pytest
import requests


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://ya.ru",
        help="URL для тестирования (по умолчанию https://ya.ru)"
    )
    parser.addoption(
        "--status_code",
        action="store",
        default=200,
        type=int,
        help="Ожидаемый код статуса ответа (по умолчанию 200)"
    )

@pytest.fixture
def url_and_status_code(request):
    url = request.config.getoption("--url")
    status_code = request.config.getoption("--status_code")
    return url, status_code

def test_url_status(url_and_status_code):
    url, expected_status_code = url_and_status_code

    # Отправляем GET-запрос на указанный URL
    response = requests.get(url)

    # Проверяем, что код статуса соответствует ожидаемому
    assert response.status_code == expected_status_code, \
        f"Ожидался статус код {expected_status_code}, но получен {response.status_code} для {url}"

