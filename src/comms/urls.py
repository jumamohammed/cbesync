from django.urls import path
from . import views

app_name = 'comms' 

urlpatterns = [
    path("", views.index, name="index")
]