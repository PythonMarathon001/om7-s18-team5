from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    path('', views.UserView.as_view()),
    path('<int:pk>', views.UserDetailView.as_view()),
    path('<int:user_id>/order/', views.UserOrderListView.as_view()),
    path('<int:user_id>/order/<int:pk>', views.UserOrderDetailView.as_view()),
    path('add/', user_create, name='user_insert'),
    path('overdue/', overdue, name='overdue'),
    path('update/<int:id>/', user_create, name='user_update'),
    path('delete/<int:id>/', user_delete, name='user_delete'),
    path('list/', user_list, name='user_list'),
    path('user_create/', user_create, name='user_create'),
]
