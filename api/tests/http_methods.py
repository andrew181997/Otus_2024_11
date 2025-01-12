import json
import requests
import os

class HttpMethods:
    """Базовый клас в котором описана логика отправки HTTP запросов"""


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
