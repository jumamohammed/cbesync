from django.urls import path
from . import views

app_name = 'schools' 

urlpatterns = [
    path("", views.index, name="dashboard")
]