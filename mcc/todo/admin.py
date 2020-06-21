from django.contrib import admin

from mcc.todo.models import Todo


class TodoAdmin(admin.ModelAdmin):
    model = Todo
    list_display = (
        "user",
        "description",
        "complete",
        "notes",
        "deadline",
        "created",
        "updated",
    )


admin.site.register(Todo, TodoAdmin)
