from django.shortcuts import render, redirect
from django.contrib import messages
from todo.models import Todo  # Import your Todo model directly

# Index page
def index(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        Todo.objects.create(title=title, description=description)
        messages.success(request, "Todo Created Successfully!")
        return redirect("todoapp:index")

    todos = Todo.objects.all().values()  # Get all todos as dictionaries
    return render(request, "todoapp/index.html", {"todos": list(todos)})

# Update page
def update(request, id):
    todo = Todo.objects.get(id=id)
    
    if request.method == "POST":
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description', '')
        todo.save()
        messages.success(request, "Todo Updated Successfully!")
        return redirect("todoapp:index")

    return render(request, "todoapp/update.html", {"todo": todo})

# Delete confirmation page
def delete_confirm(request, id):
    todo = Todo.objects.get(id=id)
    return render(request, "todoapp/delete_confirm.html", {"todo": todo})

# Actual delete
def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    messages.error(request, "Todo Deleted Successfully!")
    return redirect("todoapp:index")