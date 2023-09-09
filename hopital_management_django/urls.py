from django.contrib import admin
from django.urls import path,include


handler404 = 'core.views.custom_404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls')),
    path('auth/',include('authentications.urls')),
    path('profile/',include('personalize.urls'))
]
