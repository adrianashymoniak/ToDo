from django.urls import path

from apps.core.views import (
    ToDoViewSet,
    ToDoCreateView,
    ToDoUpdateView,
    ToDoRemoveView,
    ToDoChangeOrder,
)

urlpatterns = [
    path("all/", ToDoViewSet.as_view({"get": "list"}), name="all_tasks"),
    path("create/", ToDoCreateView.as_view(), name="create_task"),
    path("<uuid:uuid>/update/", ToDoUpdateView.as_view(), name="update_task"),
    path("re-order/", ToDoChangeOrder.as_view(), name="re_order_tasks"),
    path("<uuid:uuid>/delete/", ToDoRemoveView.as_view(), name="delete_task"),
]
