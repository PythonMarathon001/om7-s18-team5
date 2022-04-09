from django.contrib import admin
from django.urls import path, include, re_path
from .views import *
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='DreamLibra API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('user/',   include("authentication.urls"), name="user"),
    path('api/v1/', include("author.urls")),
    path('api/v1/', include("book.urls")),
    path('swagger', schema_view, name="swagger"),
    path('author/', include("author.urls"), name="author"),
    path('book/',   include("book.urls")),
    path('order/',  include("order.urls"), name="order"),
    path('statistics/', statistics, name="statistics"),
    path('rules/', rules, name="rules"),
    path('reconstruction/', reconstruction, name="reconstruction"), 
]
