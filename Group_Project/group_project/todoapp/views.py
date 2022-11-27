from pyexpat.errors import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


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
    if not x:
        return redirect('todo')
    else:
        new_item = TodoListItem(content = x)
        new_item.save()
        return redirect('todo')

def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id= i)
    y.delete()
    return redirect('todo')