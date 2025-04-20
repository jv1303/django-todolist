from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.
def index(response):
    return render(response, 'home.html', {})

def toDoList(response, id):
    ls = ToDoList.objects.filter(ukey = id)
    it = Item.objects.filter(toDoList = id)
    items_exist = True
    if not it.exists():
        items_exist = False
    if ls.exists():
        return render(response, 'todo.html', {"list": ls, "items": it, "items_exist": items_exist})
    else:
        return render(response, 'page_not_found.html')