from django.urls import path
from .views import register, user_login
app_name = 'userApp'
urlpatterns = [
    path('register/', register, name='register'),
    path('user_login/', user_login, name='user_login'),
]
