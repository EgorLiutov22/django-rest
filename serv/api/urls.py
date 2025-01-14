from django.urls import path
from . import views

urlpatterns = [
    path('datetime/', views.d_time),

]