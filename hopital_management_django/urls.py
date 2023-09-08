from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls')),
    path('auth/',include('authentications.urls')),
    path('profile/',include('personalize.urls')),
]
