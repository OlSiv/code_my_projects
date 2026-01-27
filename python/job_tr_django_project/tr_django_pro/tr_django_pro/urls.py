from django.contrib import admin
from django.urls import path

from main_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('page2/', views.page2_view), # Добавили
    path('page3/', views.page3_view)
]
