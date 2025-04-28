from django.urls import path
from app1.views import *
app_name='something'
urlpatterns=[
    path('cinema/',cinema,name='cinema'),
    path('movie/',movie,name='movie'),
]