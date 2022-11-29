from django.contrib import admin


class ToDoItemAdmin(admin.ModelAdmin):
    list_display = ("uuid", "title", "description", "status",
                    "created", "order")
    search_fields = ("title",)
