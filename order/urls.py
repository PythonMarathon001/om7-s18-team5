from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.OrderView.as_view()),
    path('<int:pk>', views.OrderDetailView.as_view()),
    path('order/<int:id>', order_create, name='order_insert'),
    path('update/<int:id>/', order_create, name='order_update'),
    path('delete/<int:id>/', order_delete, name='order_delete'),
    path('list/', order_list, name='order_list'),
    path('author_create/', order_create, name='order_create'),
]
