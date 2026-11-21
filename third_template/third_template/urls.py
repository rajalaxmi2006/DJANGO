
from django.contrib import admin
from django.urls import path , include
from firstapp import urls as first_urls
from secondapp import urls as second_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include(first_urls),),
    path('home/',include(second_urls),)
]
