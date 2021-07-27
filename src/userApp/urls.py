from django.urls import path
from .views import register
app_name = 'userApp'
urlpatterns = [
    path('register/', register, name='register'),

]
