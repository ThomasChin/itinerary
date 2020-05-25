from django.contrib import admin

# Register your models here.
from itinerary.todo.models import Todo


class TodoAdmin(admin.ModelAdmin):
    model = Todo
    list_display = ("user", "description", "notes", "deadline", "created", "updated")


admin.site.register(Todo, TodoAdmin)