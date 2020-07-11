from django.urls import path

from mcc.users.views import login_view

app_name = "users"

urlpatterns = [path("/login", login_view)]
