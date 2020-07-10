import pytest

from mcc.todo.models import Todo


@pytest.fixture()
def full_todo():
    return Todo.objects.create(
        description="Todo number 1", notes="Some additional notes"
    )


@pytest.fixture()
def description_todo():
    return Todo.objects.create(description="This Todo only has a description!")
