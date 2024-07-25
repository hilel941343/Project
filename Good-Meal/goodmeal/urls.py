
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('goodmeal/',include('goodmeal_app.urls'))
]
