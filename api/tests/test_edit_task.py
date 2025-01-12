from methods_gectaro import GectaroApi,delete_task,set_up
import pytest
import requests
api = GectaroApi()

def test_edit_task(set_up,delete_task):
    id_task =set_up
    body = {
            "project_tasks_resource_id": 14119591,
            "volume": 6666,
            "cost": 66666,
            "needed_at": 1734163804,
            "created_at": 1735134746,
        }
    result = api.edit_task(id_task,body)
    data = result.json()
    assert data.get("volume") == 6666
    assert result.status_code == 200
    delete_task(id_task)

def test_edit_task_negative(set_up,delete_task):

    body = {
            "project_tasks_resource_id": 14119591,
            "volume": 6666,
            "cost": 66666,
            "needed_at": 1734163804,
            "created_at": 1735134746,
        }
    result = api.edit_task(1234,body)
    assert result.status_code == 404
