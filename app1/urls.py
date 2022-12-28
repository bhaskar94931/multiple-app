from django.urls import path
from app1.views import *
app_name='something 1'
urlpatterns=[
    path('bunny/',bunny,name='bunny'),
    path('laddu/',laddu,name='laddu'),
]