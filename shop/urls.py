from django.urls import path

from . import views

urlpatterns = [
    # главнвая стрница
    path('', views.frontpage, name='frontpage'),
    # контакты
    path('contacts/', views.contacts, name='contacts'),
]
