from methods_gectaro import GectaroApi,delete_task
import pytest
import requests

api = GectaroApi()
request = api.add_task_project()
data = request.json()
def test_have_key(delete_task):
    """Тест для проверки наличия всех ключей у заявки"""
    expected_keys = {
        'id', 'project_tasks_resource_id', 'volume', 'cost', 'batch_number',
        'batch_parent_request_id', 'is_over_budget', 'created_at', 'updated_at',
        'user_id', 'needed_at', 'created_by', 'sort_order'
    }
    first_dict = data

    # Проверяем, что первый словарь содержит все ключи
    assert expected_keys.issubset(first_dict.keys()), f"Ключи отсутствуют в первом элементе: {first_dict}"
    print(data)
    id_task = first_dict.get("id")
    delete_task(id_task)
def test_add_task_project(delete_task):
    """Негативный тест для создания заявки в проекте с некорректным body."""
    # Передаем некорректный body
    body = {
        'project_tasks_resource_id': 14119591,
        'volume': 111,
        'cost': 111,
        'needed_at': 1734163804,
        'is_over_budget': 1
    }
    # Выполняем запрос и проверяем результат
    result = api.add_task_project(body)
    # Проверяем, что задача не создана
    assert result.status_code == 201
    assert "created_at" in result.json()
    data = result.json()
    id_task = data.get("id")
    delete_task(id_task)

def test_add_task_project_negative(delete_task):
    """Негативный тест для создания заявки в проекте с некорректным body."""
    # Передаем некорректный body
    body = {
        'project_tasks_resource_id': 14119591,
        'volume': 'aqwde',
        'cost': 111,
        'needed_at': 1734163804,
        'is_over_budget': 1
    }
    # Выполняем запрос и проверяем результат
    result = api.add_task_project(body)
    # Проверяем, что задача не создана
    assert result.status_code == 422