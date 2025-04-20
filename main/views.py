from django.shortcuts import render
from .models import ToDoList, Item

# Create your views here.
def index(request):
    return render(request, 'home.html', {})

def toDoList(request, id):
    ls = ToDoList.objects.filter(ukey = id)
    it = Item.objects.filter(toDoList = id)
    items_exist = True
    if not it.exists():
        items_exist = False
    if ls.exists():
        return render(request, 'todo.html', {"list": ls, "items": it, "items_exist": items_exist})
    else:
        return render(request, 'page_not_found.html')
    
def lists(request):
    ls = ToDoList.objects.all()
    return render(request, 'lists.html', {"lists": ls})