from django.contrib import admin
from django.urls import path
from polls import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('min', views.getMinT),
    path('max', views.getMaxT),
    path('average', views.getAverageT)
]
