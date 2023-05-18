from django.urls import path
from . import views
urlpatterns = [
    path('' , views.dashboard , name='dashboard'),
    path('<str:stock>/' , views.get_stock , name ='get_stock'),
    path('vn30/<str:time_range>/' , views.get_vn30 , name = 'get_vn30'),
]
