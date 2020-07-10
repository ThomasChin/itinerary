from django.test import Client
import pytest


BASE_URL = "/api/v1/todo"


@pytest.mark.django_db
def test_list_todos(client: Client, full_todo, description_todo):
    # TODO: Change when implement User filtering of todos.
    r = client.get(BASE_URL + "/list")
    assert 200 == r.status_code
    body = r.json()


@pytest.mark.django_db
def test_create_todo(client: Client):
    r = client.get(BASE_URL + "/list")
    pass


def test_create_todo_duplicate():
    pass


def test_create_todo_invalid_parameters():
    pass


def test_get_todo():
    pass


def test_update_todo():
    pass


def test_delete_todo():
    pass
