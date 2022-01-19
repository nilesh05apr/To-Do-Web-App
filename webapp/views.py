from asyncio import tasks
from django.shortcuts import render, HttpResponse
from matplotlib.pyplot import title
from .models import Task
from .forms import TaskForm
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            code = request.POST.get('code')
            title = request.POST.get('title')
            description = request.POST.get('description')
            deadline = request.POST.get('deadline')
            status = request.POST.get('status')
            instance = Task(code = code,title = title, description = description, deadline = deadline, status = status)
            instance.save()
            tasks = Task.objects.all()
            form = TaskForm()
            context = {
                'tasks': tasks,
                'form' : form
             }
        return render(request,'webapp/index.html',context)
    else :
        form = TaskForm()
        tasks = Task.objects.all()
        context = {
            'tasks': tasks,
            'form' : form
        }
        return render(request,'webapp/index.html',context)

def completed(request):
    form = TaskForm()
    task = Task.objects.all().filter(status="True")
    context = {
        'tasks':task,
        'form':form
    }
    return render(request,'webapp/index.html',context)

def incompleted(request):
    form = TaskForm()
    task = Task.objects.all().filter(status="False")
    context = {
        'tasks':task,
        'form':form
    }
    return render(request,'webapp/index.html',context)

def mark_complete(request,p_id):
    task = Task.objects.get(id=p_id)
    task.status = True
    task.save()
    tasks = Task.objects.all()
    form = TaskForm()
    context = {
        'tasks': tasks,
        'form': form
    }
    return render(request,'webapp/index.html',context)