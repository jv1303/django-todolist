from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Home"),
    path("lists/<str:id>/", views.toDoList, name="To Do List"),
    path("lists/", views.lists, name="Lists"),
    path("createlist/", views.create, name="Create"),
    path("deletelist/", views.deletelist, name="delete-list")
]