from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Home"),
    path("todo<str:id>/", views.toDoList, name="To Do List")
]