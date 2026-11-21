from django.urls import path
from . import views

app_name="secondapp"

urlpatterns=[
    path('test/',views.home, name='home')
]