from django.shortcuts import render,redirect
from .models import Notes
# Create your views here.
from .forms import NotesForm

def  list(request):
    all_notes=Notes.objects.all()
    return render(request,'note_list.html',{'notes':all_notes})

def detail(request,id):
    note=Notes.objects.get(pk=id)
    return render(request,'note_detail.html',{'note':note})

def create_note(request):
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            note = form.save()
            return redirect('notelist')
    else:
        form = NotesForm()

    return render(request, 'note_form.html', {'form': form})


def update_note(request, id):
    note = Notes.objects.get(pk=id)

    if request.method == 'POST':
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notelist')
    else:
        form = NotesForm(instance=note)

    return render(request, 'update_form.html', {'form': form})

def delete_note(request, id):
    note = Notes.objects.get(pk=id)

    if request.method == 'POST':
        note.delete()
        return redirect('notelist')

    return render(request, 'delete_conform.html', {'note': note})

