from django.urls import path
from . import views
from . views import register_user

urlpatterns = [
    path('', views.login_user, name='login'), 
    # path('register/', views.register_user, name='register'), 
    path('register/', register_user.as_view(), name='register'), 
]