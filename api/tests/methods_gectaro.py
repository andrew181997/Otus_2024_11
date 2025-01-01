import pytest
import requests
from BaseCase import HttpMethods

h = HttpMethods()

class TasksApi:
    @staticmethod
    def add_task_project():
        """Метод создания заявки в проекте"""
        body = {
            'project_tasks_resource_id': 14119591,
            'volume': 101,
            'cost':100,
            'needed_at': 1735134746,
            'is_over_budget': 1
        }
        result = HttpMethods.post(url=h.BASE_URL+h.project+h.project_id+h.resource_requests,header= h.headers, body=body)
        data = result.json()
        id = data.get("id")
        return result.status_code, result.json(), id

    @staticmethod
    def get_tasks_project():
        """Метод получения списка заявок в проекте"""
        result = HttpMethods.get(url=h.BASE_URL+h.project+h.project_id+h.resource_requests,header= h.headers)
        return result.status_code, result.json()

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
        result = HttpMethods.post(url=h.BASE_URL+h.companies+h.company_id+h.resource_requests,header= h.headers, body=body)
        return result.status_code, result.json()

    @staticmethod
    def get_tasks_company():
        """Метод получения списка заявок в компании"""
        result = HttpMethods.get(url=h.BASE_URL+h.companies+h.company_id+h.resource_requests,header= h.headers)
        return result.status_code, result.json()


    def get_tasks_info(self,id):
        """Метод получения информации по заявке в проекте"""
        result = HttpMethods.get(url=h.BASE_URL+h.project+h.project_id+h.resource_requests +id,header= h.headers)
        return result.status_code, result.json(), result.url

    @staticmethod
    def del_task():
        """Метод удаления заявки в проекте"""
        status, response , id = TasksApi.add_task_project()
        id_task ='/'+str(id)
        result = HttpMethods.delete(url=h.BASE_URL + h.project + h.project_id + h.resource_requests +id_task, header=h.headers)
        if result.status_code == 204:
            return  result.status_code, result.url
        else:
            ValueError(f'Error! {result.status_code}')

    @staticmethod
    def edit_task():
        """Метод изменения заявки в компании"""
        status, response, id = TasksApi.add_task_project()
        id_task = '/' + str(id)
        body = {
            "project_tasks_resource_id": 14119591,
            "volume": 999,
            "cost": 9999,
            "needed_at": 1734250125,
            "created_at": 1735134746,
        }
        result = HttpMethods.put(url=h.BASE_URL + h.project + h.project_id + h.resource_requests + id_task , body=body, header=h.headers)
        if result.status_code == 200:
            return  result.json(), result.url
        else:
            ValueError(f'Error! {result.status_code}')

print(TasksApi.get_tasks_project())