import json
import requests
import os

class HttpMethods:
    """Базовый клас в котором описана логика отправки HTTP запросов"""
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
    id_for_task ='/10419041'

    @staticmethod
    def get(url: str, header: dict) -> requests.Response:
        """
        Метод для отправки базового get
        :param url: url
        :param header: заголовки
        :return:  Объект ответа библиотеки requests
        """
        result = requests.get(url, headers=header)
        return result

    @staticmethod
    def post(url: str, body: json, header: dict[str: str]) -> requests.Response:
        """
        Метод для отправки базового post
        :param url: url
        :param body: тело запроса (json)
        :param header: заголовки
        :return:  Объект ответа библиотеки requests
        """
        result = requests.post(url, json=body, headers=header)
        return result

    @staticmethod
    def delete(url, header) -> requests.Response:
        """
        Метод для отправки базового delete
        :param url: url
        :param header: заголовки
        :return:  Объект ответа библиотеки requests
        """
        result = requests.delete(url, headers=header)
        return result

    @staticmethod
    def put(url, body,header) -> requests.Response:
        """
        Метод для отправки базового put
        :param url: url
        :param body: тело запроса (json)
        :return:  Объект ответа библиотеки requests
        """
        result = requests.put(url, json=body, headers=header)
        return result
