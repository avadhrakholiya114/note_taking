from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# avadh121
def home(request):
    return render(request,'home/home.html')

