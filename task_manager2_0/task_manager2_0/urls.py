from django.conf import settings
from users.views import user_create
from api.views import TaskViewSet, ProjectViewSet
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views
v1_router = routers.DefaultRouter()

v1_router.register(r"task", TaskViewSet, basename="tasks")
v1_router.register(r"project", ProjectViewSet, basename="projects")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_user/', user_create, name='create-user'),
    path('api-token-auth/', views.obtain_auth_token, name='api_token_auth'),
    path('api/v1/', include(v1_router.urls)),
]