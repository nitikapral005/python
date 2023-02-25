from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name="index"),
    # path('nextt/', nextt, name= "nextt"),
    path('update_data/<int:id>', updateuser, name="update_data"),
    path('delete_data/<int:id>', deleteuser, name="delete_data"),
    path('register/', registeruser, name="register"),
    path('login/', loginuser, name="login"),
    path('logout/', logoutuser, name="logout"),

]
