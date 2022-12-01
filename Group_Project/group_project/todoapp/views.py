
from django.shortcuts import render, redirect


from . models import TodoListItem

# Create your views here.

# function used to render the todo html page and add the dict of to-dos
def todoappView(request):
    # gathers the todo obects from model.py
    all_todo_items = TodoListItem.objects.all() 
    # adds all todo items/objects into a dict for the html page to display
    todos = {
        "all_items": all_todo_items
    }
    return render(request, 'todo.html', todos)


# function used to add a todo item/object to the users todo list
def add_todoView(request):
    add_todo = request.POST['content']
    if not add_todo:
        return redirect('todo')
    else:
        new_item = TodoListItem(content = add_todo)
        new_item.save()
        return redirect('todo') # redirects the endpoint to the todo.html page


# function that will aloow the user to delete a todo item/object from their 
# todo list.
def deleteTodoView(request, i):
    delete_todo = TodoListItem.objects.get(id= i)
    delete_todo.delete()
    return redirect('todo') # redirects the endpoint to the todo.html page