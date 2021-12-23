from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

# Create your views here.

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {
        "tasks" : tasks,
        "form" : form
    }
    return render(request, "tasks/list.html", context)

def update(request, pk):

    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "task" : task,
        "form" : form
    }
    return render(request, "tasks/update_task.html", context)

def delete(request, pk):

    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.delete()
        return redirect("index")
        
    return render(request, "tasks/confirm.html", {"task" : task})