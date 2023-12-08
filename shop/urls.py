from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    # главнвая стрница
    path('', views.frontpage, name='frontpage'),
    # товар
    path('<int:pk>/', views.products, name='detail'),
    # товар
    path('add-product', views.add_product, name='add'),
]
