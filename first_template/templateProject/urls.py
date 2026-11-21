
from django.contrib import admin
from django.urls import path

from testApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home_view),
    path('about/', views.about_view),
    path('contact/', views.contact_view),
    path('login/', views.login_view),
    path('signup/', views.signup_view)
]
