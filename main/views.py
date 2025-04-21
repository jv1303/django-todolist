from django.shortcuts import render
from .models import ToDoList, Item
from .forms import CreateNewList
import random
import string

# Create your views here.
def index(response):
    return render(response, 'home.html', {})

def toDoList(response, id):
    ls_query = ToDoList.objects.filter(ukey = id)
    it = Item.objects.filter(toDoList = id)
    items_exist = True
    if not it.exists():
        items_exist = False
    if ls_query.exists():
        ls = ToDoList.objects.get(ukey = id)
        return render(response, 'todo.html', {"list": ls, "items": it, "items_exist": items_exist})
    else:
        return render(response, 'page_not_found.html')
    
def lists(response):
    ls = ToDoList.objects.all()
    return render(response, 'lists.html', {"lists": ls})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            uk = 0
            while uk == 0:
                charset = string.ascii_letters + string.digits
                rand_ukey = ''.join(random.choices(charset, k=10))
                ls_query = ToDoList.objects.filter(ukey__exact=rand_ukey)
                if not ls_query:
                    uk = rand_ukey
                else:
                    uk = 0
            
            n = form.cleaned_data["name"]
            t = ToDoList(ukey=uk, name=n)
            t.save()
            result = "List registered sucefully!"
        else:
            result = "An error ocourred and the list was not registered."
        
    else:
        form = CreateNewList()
        result = ""

    return render(response, 'create.html', {"form": form, "result": result})