from django.urls import path
from . import views

app_name="firstapp"

urlpatterns=[
    path('test/',views.index_view, name='index')
]