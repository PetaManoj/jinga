from django.urls import path
from app.views import *
app_name='nothing'
urlpatterns=[
    path('captain/',captain,name='captain'),
    path('jinga/',jinga,name='jinga'),
]