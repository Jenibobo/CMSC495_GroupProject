from django.http import HttpResponseRedirect
from django.shortcuts import render

from . models import TodoListItem

# Create your views here.
def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    todos = {
        "all_items": all_todo_items
    }
    return render(request, 'todo.html', todos)


def add_todoView(request):
    x = request.POST['content']
    new_item = TodoListItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/homeapp/todos/')


def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/homeapp/todos/')