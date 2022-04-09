from django.urls import path, include
from .views import *
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register("author", AuthorViewAPI)
                
urlpatterns = [
    # path('author', AuthorList.as_view(), name='author'),
    # path('', include(router.urls)),
    path('', AuthorViewAPI.as_view()),
    path('<int:pk>', AuthorDetailViewAPI.as_view()),    
    path('', author_create, name = 'author_insert'),
    path('<int:id>/',author_create, name='author_update'),
    path('delete/<int:id>/', author_delete, name='author_delete'),
    path('list/', author_list, name='author_list'),
    path('author_create/', author_create, name='author_create'),
]
