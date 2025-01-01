from methods_gectaro import TasksApi
import pytest
import requests

def test_status_code():
    code , json = TasksApi.get_tasks_project()
    assert code == 200

def test_have_key():
    code , json = TasksApi.get_tasks_project()
    expected_keys = {
        'id', 'project_tasks_resource_id', 'volume', 'cost', 'batch_number',
        'batch_parent_request_id', 'is_over_budget', 'created_at', 'updated_at',
        'user_id', 'needed_at', 'created_by', 'sort_order'
    }
    first_dict = json[0]
    # Проверяем, что первый словарь содержит все ключи
    assert expected_keys.issubset(first_dict.keys()), f"Ключи отсутствуют в первом элементе: {first_dict}"

def test_status_code1():
    code , json = TasksApi.get_tasks_project()
    # Проврека что в ответе сервера приходит 20 заявок за пагинацию
    assert (len(json)) == 20