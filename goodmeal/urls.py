
from django.contrib import admin
from django.urls import path, include
from goodmeal_app import views as goodmeal_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',goodmeal_views.index, name='index'),
    path('goodmeal/',include('goodmeal_app.urls')),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
