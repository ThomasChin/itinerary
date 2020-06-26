from django.contrib import admin

from mcc.todo.models import Todo


class TodoAdmin(admin.ModelAdmin):
    model = Todo
    list_display = (
        "user",
        "description",
        "done",
        "notes",
        "deadline",
        "created",
        "updated",
        "started_at",
        "finished_at",
    )


admin.site.register(Todo, TodoAdmin)
