from django.urls import path
from .views import register, user_login, user_logout, profile

app_name = 'userApp'
urlpatterns = [
    path('register/', register, name='register'),
    path('user_login/', user_login, name='user_login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
]
