from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    # главнвая стрница
    path('', views.frontpage, name='frontpage'),
    # подробная страница товаров
    path('<int:pk>/', views.ProductDetailView.as_view(), name='detail'),
    # добавить товар
    path('add-product', views.add_product, name='add'),
    # обновить товар
    path('update-product/<int:pk>/', views.update_product, name='update'),
    # удалить товар
    path('delete-product/<int:pk>/', views.ProductDeleteView.as_view(), name='delete'),
    # успешная оплата
    path('success/', views.PaymentSuccessView.as_view(), name='success'),
    # отмена оплата
    path('cancel/', views.PaymentCancelView.as_view(), name='cancel'),
    # оплата
    path('api/checkout-session/<int:id>/', views.create_checkout_session, name='api_checkout_session'),
]
