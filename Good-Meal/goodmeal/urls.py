
from django.contrib import admin
from django.urls import path, include
from goodmeal_app import views as goodmeal_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',goodmeal_views.index, name='index'),
    path('goodmeal/',include('goodmeal_app.urls')),
]
