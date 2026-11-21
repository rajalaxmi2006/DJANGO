
from django.contrib import admin
from django.urls import path
from testapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_view),
    path('u/<str:username>/', views.username),
    path('add/<int:first>/<int:second>/', views.add),
    path('prime/<int:number>/', views.check_prime_view),
]
