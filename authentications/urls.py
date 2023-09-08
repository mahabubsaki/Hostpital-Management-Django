from django.urls import path
from .views import auth_login,auth_signup,auth_logout
urlpatterns = [
    path('login/',auth_login,name='login'),
    path('signup/',auth_signup,name='signup'),
    path('logout/',auth_logout,name="logout")
]