from django.urls import path, include
from . import views
from . views import home, car_details
# from . import include

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('addcar/', views.add_car, name='add_car'), 
    path('car_details/<int:pk>', car_details.as_view(), name='car_details'),

]