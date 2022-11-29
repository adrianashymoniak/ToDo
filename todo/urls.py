from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="ToDo API",
        default_version="v1",
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/v1/docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("api/v1/auth/", include("apps.accounts.urls")),
    path("api/v1/to-do/", include("apps.core.urls")),
]
