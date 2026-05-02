from django.shortcuts import render
from django.http import HttpResponseRedirect

from todo_app.models import Todo

# Create your views here.


def todo_list(request):
    todos = Todo.objects.all()
    return render(
        request,
        "todo_list.html",
        {"todos": todos},
    )


def todo_delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return HttpResponseRedirect("/")


def todo_create(request):
    print(request.method, request.POST)
    return render(request, "todo_create.html")
