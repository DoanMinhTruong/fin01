from django.urls import path
from . import views
urlpatterns = [
    # path('' , views.index),
    path('register/', views.register , name='user_register'),
    path('login/', views.login, name='user_login'),
    path('logout/' , views.logout_view , name='user_logout'),
]
