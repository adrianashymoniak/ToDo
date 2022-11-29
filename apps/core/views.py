from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.core.models import TodoItem
from apps.core.permissions import IsOwnerOrReadOnly
from apps.core.serializers import TodoItemSerializer, ToDoItemOrderSerializer


class ToDoViewSet(ReadOnlyModelViewSet):
    serializer_class = TodoItemSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def list(self, request, *args, **kwargs):
        queryset = TodoItem.objects.filter(user=request.user).order_by("order")
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ToDoCreateView(CreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)


class ToDoUpdateView(UpdateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    lookup_field = "uuid"
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    http_method_names = ["put"]


class ToDoRemoveView(DestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    lookup_field = "uuid"
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)


class ToDoChangeOrder(APIView):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    @swagger_auto_schema(request_body=ToDoItemOrderSerializer)
    def put(self, request):
        tasklist = request.data.get("tasks")
        if tasklist:
            order_id = 1
            for uuid in tasklist:
                try:
                    task = TodoItem.objects.get(uuid=uuid)
                    task.order = order_id
                    task.save()
                    order_id += 1
                except TodoItem.DoesNotExist:
                    pass

        return Response(status=status.HTTP_202_ACCEPTED)
