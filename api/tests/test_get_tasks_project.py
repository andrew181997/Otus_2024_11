from methods_gectaro import GectaroApi, set_up,delete_task

import pytest
import requests
request = GectaroApi.get_tasks_project()
data = request.json()
def test_status_code():
    assert request.status_code == 200

def test_have_key():
    """Тест для проверки наличия всех ключей у заявки"""
    expected_keys = {
        'id', 'project_tasks_resource_id', 'volume', 'cost', 'batch_number',
        'batch_parent_request_id', 'is_over_budget', 'created_at', 'updated_at',
        'user_id', 'needed_at', 'created_by', 'sort_order'
    }
    first_dict = data[0]
    # Проверяем, что первый словарь содержит все ключи
    assert expected_keys.issubset(first_dict.keys()), f"Ключи отсутствуют в первом элементе: {first_dict}"

def test_status_code1():
    """ Проврека что в ответе сервера приходит 20 заявок за пагинацию"""

    assert (len(data)) == 20


def test_get_task_info(set_up,delete_task):
    """Тест для проверки информации по заявке"""
    api = GectaroApi()
    task_id = set_up  # Получаем id заявки из фикстуры
    result = api.get_tasks_info(task_id)  # Передаем id заявки
    assert result.status_code == 200  # Проверяем статус ответа
    assert "id" in result.json()  # Проверяем, что id присутствует в ответе
    assert result.json()["id"] == task_id  # Проверяем, что id совпадают
    delete_task(task_id)




# def test_task_creation_and_deletion(delete_task):
#     """Тест для проверки создания и удаления заявки в компании."""
#     # 1. Создаем заявку
#     api = GectaroApi()
#     status_code, response_data = api.add_task_company()
#     assert status_code == 201  # Проверяем, что заявка успешно создана
#
#     # Получаем ID созданной заявки
#     task_id = response_data.get("id")
#     assert task_id is not None, "Task ID is None!"
#
#     # 2. Выполняем тестовые проверки
#     # Например, проверяем информацию о заявке (добавьте соответствующий метод)
#
#     # 3. Удаляем заявку через фикстуру
#     delete_task(task_id)
#
#     # 4. Проверяем, что заявка успешно удалена
#     # Проверка через метод получения информации о заявке, который должен вернуть 404
#     try:
#         api.get_tasks_info(task_id)
#     except Exception as e:
#         assert "404" in str(e), f"Expected 404 error for task {task_id}, but got: {str(e)}"