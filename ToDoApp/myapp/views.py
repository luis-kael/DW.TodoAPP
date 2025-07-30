from django.shortcuts import render,redirect,get_object_or_404
from .models import TodoModel
# Create your views here.

def TodoList(request):
    todo = TodoModel.objects.all()
    contex = {
        'todo':todo
    }
    return render(request, 'index.html',contex)
# Create Function
def TodoCreate(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        completed = request.POST.get('completed') == 'on'

        TodoModel.objects.create(
            title=title,
            description=description,
            completed=completed
        )

        return redirect('ToDoList')
    return render(request, 'todo_form.html')

# Detail Function
def TodoDetail(request, pk):
    todo = get_object_or_404(TodoModel, pk=pk)
    return render(request, 'todo_detail.html', {'todo': todo})

#Update Function
def TodoUpdate(request, pk):
    todo = get_object_or_404(TodoModel, pk=pk)

    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.completed = request.POST.get('completed') == 'on'
        todo.save()
        return redirect('TodoList')
    return render(request, 'todo_form.html', {'todo':todo})

# Delete Function
def TodoDelete(request, pk):
    todo =  get_object_or_404(TodoModel, pk=pk)

    if request.method == 'POST':
        todo.delete()
        return redirect('TodoList')
    return render(request, 'index.html',{'todo':todo})
    