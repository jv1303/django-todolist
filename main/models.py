from django.db import models

# Create your models here.
class ToDoList(models.Model):
    ukey = models.CharField(max_length=20, primary_key = True, serialize=False)
    name = models.CharField(max_length=200)

    def get_name(self):
        return self.name

class Item(models.Model):
    ukey = models.CharField(max_length=20, primary_key=True, serialize=False)
    toDoList = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    complete = models.BooleanField()

    def get_text(self):
        return self.text