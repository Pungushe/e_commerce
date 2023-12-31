from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # админка
    path('admin/', admin.site.urls),
    # главная страница
    path('', include('shop.urls', namespace='shop')),
    # главная страница
    path('users/', include('users.urls', namespace='users')),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
