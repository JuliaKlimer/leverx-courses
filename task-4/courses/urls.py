from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('', include("classroom.urls")),
    path('admin/', admin.site.urls),
    path('api/', schema_view),
    path('api-auth/', include("rest_framework.urls", namespace='rest_framework')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
