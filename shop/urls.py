from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    # главнвая стрница
    path('', views.ProductListView.as_view(), name='frontpage'),
    # подробная страница товаров
    path('<int:pk>/', views.ProductDetailView.as_view(), name='detail'),
    # добавить товар
    path('add-product', views.add_product, name='add'),
    # обновить товар
    path('update-product/<int:pk>/', views.update_product, name='update'),
    # удалить товар
    path('delete-product/<int:pk>/', views.delete_product, name='delete'),
]
