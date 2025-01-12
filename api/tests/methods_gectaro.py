import pytest
import requests
import os
from http_methods import HttpMethods

token = os.getenv("API_KEY")
headers = {'Authorization': f'Bearer 5gtzAWntym3oDFjBQTKP8Jb2WP-S3Thb',
           'Content-Type': 'application/json',
           'Accept': "application/json"}
BASE_URL = "https://api.gectaro.com/v1/"
project_id = '/106728'
company_id = '/7323'
resource_requests = '/resource-requests'
project = 'projects'
companies = 'companies'
id_for_task = '/10419041'

@pytest.fixture(autouse=False,scope="function")
def set_up():
    api = GectaroApi()
    result= api.add_task_project()
    data = result.json()
    id = data.get("id")
    yield id

@pytest.fixture(scope="function")
def delete_task():
    """Фикстура для удаления заявки."""
    def _delete_task(task_id):
        """Удаляет заявку по ID, используя метод del_task."""
        api = GectaroApi()  # Создаем экземпляр класса
        result = api.del_task(task_id)
        assert result.status_code == 204, f"Failed to delete task with ID {task_id}. Status: {result.status_code}"
    return _delete_task


class GectaroApi(HttpMethods):

    def add_task_project(self, body=None):
        """Метод создания заявки в проекте"""
        default_body = {
            'project_tasks_resource_id': 14119591,
            'volume': 151515,
            'cost':100,
            'needed_at': 1734163804,
            'is_over_budget': 1
        }
        self.body = body if body else default_body
        result = HttpMethods.post(url=BASE_URL+project+project_id+resource_requests, header=headers, body=self.body)
        # data = result.json()
        # id = data.get("id")
        return result

    @staticmethod
    def get_tasks_project():
        """Метод получения списка заявок в проекте"""
        result = HttpMethods.get(url=BASE_URL+project+project_id+resource_requests, header=headers)
        return result

    @staticmethod
    def add_task_company():
        """Метод создания заявки в компании"""
        body = {
            'project_tasks_resource_id': 14119591,
            'volume': 101,
            'cost':100,
            'needed_at': 1735134746,
            'is_over_budget': 1
        }
        result = HttpMethods.post(url=BASE_URL+companies+company_id+resource_requests, header=headers, body=body)
        return result

    @staticmethod
    def get_tasks_company():
        """Метод получения списка заявок в компании"""
        result = HttpMethods.get(url=BASE_URL+companies+company_id+resource_requests,header= headers)
        return result


    def get_tasks_info(self,id):
        """Метод получения информации по заявке в проекте"""
        result = HttpMethods.get(url=f"{BASE_URL}{project+project_id}{resource_requests}/{str(id)}",header= headers)
        return result


    def del_task(self,id):
        """Метод удаления заявки в проекте"""
        result = HttpMethods.delete(url=f"{BASE_URL}{project+project_id}{resource_requests}/{str(id)}", header=headers)
        return result


    def edit_task(self,id,body=None):
        """Метод изменения заявки в компании"""

        default_body = {
            "project_tasks_resource_id": 14119591,
            "volume": 999,
            "cost": 9999,
            "needed_at": 1734250125,
            "created_at": 1735134746,
        }
        self.body = body if body else default_body
        result = HttpMethods.put(url=f"{BASE_URL}{project+project_id}{resource_requests}/{str(id)}", body=self.body, header=headers)
        return result

