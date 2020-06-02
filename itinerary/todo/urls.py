from django.urls import path

from itinerary.todo.views import TodoListView

app_name = "todo"

urlpatterns = [
    path("/list", TodoListView.as_view()),
]
