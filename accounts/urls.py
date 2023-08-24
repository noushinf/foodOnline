from django.urls import path, include
from . import views


urlpatterns = [
    # path('', views.myAccount),
    path('registerUser/', views.registerUser, name='registerUser'),
]