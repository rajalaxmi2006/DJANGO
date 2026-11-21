from litapp import views
from django.contrib import admin
from django.urls import path 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home_view),
    path('exam/',views.exam_view)
]