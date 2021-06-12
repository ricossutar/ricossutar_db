from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_db import views
from rest_db import urls as rest_urls

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('', include(rest_urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]

