from django.urls import path, include
from .views import *
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register("book", BookViewAPI)

urlpatterns = [
    #path("", include(router.urls)),
    path('', BookViewAPI.as_view()),
    path('<int:pk>', BookDetailViewAPI.as_view()), 
    path('add/', book_form, name='book_insert'),
    path('list/', BookListAll.as_view(), name='list_all'),
    #path('<int:book_id>/', by_id, name='by_id'),
    path('<int:id>/', book_form, name='book_update'),
    path('delete/<int:id>/', book_delete, name='book_delete'),
    path('unordered/', unordered, name='unordered'),
    path('book_list/', BookListSearch.as_view(), name='book_list'),

]
