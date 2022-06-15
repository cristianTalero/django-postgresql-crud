from django.shortcuts import redirect, render, Http404, HttpResponse
from .forms import NewTask, EditTask
from .models import Task
from django.db.models import ObjectDoesNotExist


def index(request):
    tasks = Task.objects.all()

    return render(request, 'index.html', {
        'tasks': tasks,
        'uri': 'index'
    })


def show_task(request, id):
    try:
        task = Task.objects.get(pk=id)

    except ObjectDoesNotExist:
        return HttpResponse('<h1>Doesn\'t exists!</h1>')

    return render(request, 'show.html', {'task': task})


# Create your views here.
def create_task(request):
    new_task = NewTask()

    return render(request, 'create.html', {
        'new_task': new_task,
        'uri': 'create'
    })


def edit_task(request, id):
    try:
        task = Task.objects.get(pk=id)

    except ObjectDoesNotExist:
        return HttpResponse('<h1>Doesn\'t exists!</h1>')

    task_form = EditTask(
        initial={
            'title': task.title,
            'description': task.description,
            'status': task.status
        }
    )

    return render(request, 'edit.html', {
        'task': task,
        'task_form': task_form
    })


def saved_edited_task(request):
    id = request.POST.get('id')
    title = request.POST.get('title')
    description = request.POST.get('description')
    status = request.POST.get('status')

    try:
        Task.objects.update_or_create(
            id=id,
            defaults={
                'title': title,
                'description': description,
                'status': True if status == "on" else False
            }
        )
    except ObjectDoesNotExist:
        raise Http404

    return redirect('task', id=id)


def save_task(request):
    title = request.POST.get('title')
    description = request.POST.get('description')

    new_task = Task(
        title=title,
        description=description
    )

    try:
        new_task.save()
    except:
        print('An error ocurred')

    return redirect('task', id=new_task.id)


def delete_task(request, id):
    try:
        task = Task.objects.get(id=id)
        task.delete()
        status = True
    except ObjectDoesNotExist:
        status = False

    return render(request, 'delete.html', {
        'status': status
    })
