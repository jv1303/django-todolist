from django.shortcuts import render, redirect
from .models import ToDoList, Item
from .forms import CreateNewList
from .funcs import gen_ukey

# Create your views here.
def index(response):
    return render(response, 'home.html', {})

def toDoList(response, id):
    ls_query = ToDoList.objects.filter(ukey = id)
    result = ""
    color = ""

    if response.method == "POST" and ls_query.exists():
        list = ToDoList.objects.get(ukey = id)
        if response.POST.get("save"):
            for item in list.item_set.all():
                if response.POST.get("c" + str(item.ukey)):
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        elif response.POST.get("addItem"):
            txt = response.POST.get("newItem")
            if len(txt) > 0 and len(txt) < 200:
                uk = gen_ukey(8, Item, 'it')
                if response.POST.get("newCheck"):
                    compl = True
                else:
                    compl = False
                
                list.item_set.create(ukey = uk, text = txt, complete = compl)
            else:
                result = "Item text is required!"
                color = "#800"

    it = Item.objects.filter(toDoList = id)
    items_exist = True

    if not it.exists():
        items_exist = False
    if ls_query.exists():
        ls = ToDoList.objects.get(ukey = id)
        return render(response, 'todo.html', {"list": ls, "items": it, "items_exist": items_exist, "result": result, "color": color})
    else:
        return render(response, 'page_not_found.html')
    
def lists(response):
    ls = ToDoList.objects.all()
    return render(response, 'lists.html', {"lists": ls})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            uk = gen_ukey(8, ToDoList, 'td')
            n = form.cleaned_data["name"]
            t = ToDoList(ukey=uk, name=n)
            t.save()
            result = "List registered sucefully!"
            color = "#079e64"
        else:
            result = "The list must have a name."
            color = "#800"
        
    else:
        form = CreateNewList()
        result = ""
        color = "#000"

    return render(response, 'create.html', {"form": form, "result": result, "color": color})

def deletelist(response):
    id = response.POST.get("list")
    if response.method == "POST":
        list = ToDoList.objects.get(ukey = id)
        list.delete()
    
    return redirect('Lists')