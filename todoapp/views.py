from django.shortcuts import render, redirect
import requests
from django.contrib import messages

# Index page
def index(request):
    if request.method == "POST":
        data = request.POST
        requests.post("http://127.0.0.1:8000/api/createtodo", data=data)
        messages.success(request, "Todo Created Successfully!")
        return redirect("todoapp:index")  # updated to use namespace

    todos = requests.get("http://127.0.0.1:8000/api/showtodos").json()
    return render(request, "todoapp/index.html", {"todos": todos})  # template path includes app folder

# Update page
def update(request, id):
    todo = requests.get(f"http://127.0.0.1:8000/api/getonetodo/{id}").json()
    if request.method == "POST":
        requests.put(f"http://127.0.0.1:8000/api/updatetodo/{id}", data=request.POST)
        messages.success(request, "Todo Updated Successfully!")
        return redirect("todoapp:index")  # updated to use namespace

    return render(request, "todoapp/update.html", {"todo": todo})  # template path includes app folder

# Delete confirmation page
def delete_confirm(request, id):
    todo = requests.get(f"http://127.0.0.1:8000/api/getonetodo/{id}").json()
    return render(request, "todoapp/delete_confirm.html", {"todo": todo})  # template path includes app folder

# Actual delete
def delete(request, id):
    requests.delete(f"http://127.0.0.1:8000/api/deletetodo/{id}")
    messages.error(request, "Todo Deleted Successfully!")
    return redirect("todoapp:index")  # updated to use namespace
