from django.shortcuts import render
from .models import Notes
# Create your views here.
def  list(request):
    all_notes=Notes.objects.all()
    return render(request,'note_list.html',{'notes':all_notes})

def detail(request,id):
    note=Notes.objects.get(pk=id)
    return render(request,'note_detail.html',{'note':note})
    