from django.urls import path

from mcc.todo.views import TodoListView, TodoDetailView

app_name = "todo"

urlpatterns = [
    path("/list", TodoListView.as_view()),
    path("/<int:todo_id>", TodoDetailView.as_view()),
]
