from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # админка
    path('admin/', admin.site.urls),
    # главная страница
    path('', include('shop.urls', namespace='shop')),
]
