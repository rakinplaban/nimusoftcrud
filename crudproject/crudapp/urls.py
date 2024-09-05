from .views import *
from django.urls import path   
# from django.contrib.auth import login
# from django.contrib.auth import logout

urlpatterns = [
    path('', index, name='index'),
    # path('login/', login, name='login'),
    # path('register/', register, name='register'),
    # path('logout/', logout, name='logout'),
    # path('profile/', profile, name='profile'),
    # path('profile/update/', profile_update, name='profile_update'),
    # path('profile/update/password/', profile_update_password, name='profile_update_password'),
    # path('profile/update/avatar/', profile_update_avatar, name='profile_update_avatar'),
    # path('profile/delete/', profile_delete, name='profile_delete'),
]