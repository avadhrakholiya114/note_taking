from django.shortcuts import render,redirect
from .models import Notes
# Create your views here.
from .forms import NotesForm,Registerform
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages


@login_required(login_url="custom_login")
def  list(request):
    all_notes=Notes.objects.filter(user=request.user)
    return render(request,'note_list.html',{'notes':all_notes})

@login_required(login_url="custom_login")
def detail(request,id):
    note=Notes.objects.get(pk=id)
    return render(request,'note_detail.html',{'note':note})

@login_required(login_url="custom_login")
def create_note(request):
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('notelist')
    else:
        form = NotesForm()

    return render(request, 'note_form.html', {'form': form})

@login_required(login_url="custom_login")
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

@login_required(login_url="custom_login")
def delete_note(request, id):
    note = Notes.objects.get(pk=id)

    if request.method == 'POST':
        note.delete()
        return redirect('notelist')

    return render(request, 'delete_conform.html', {'note': note})


def regi(request):
    # jayare signup per click kare tayaare
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = Registerform(request.POST)
        if form.is_valid():
            # database ma user save thay jai
            form.save()

            return redirect('custom_login')
    else:
        # form = UserCreationForm()
        form = Registerform()
    return render(request, 'register.html', {'form': form})


def login_form(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # messages.success(request, f'Welcome, {username}!')
                return redirect('notelist')  # Change this to the desired URL after login
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def Logout_user(request):
    logout(request)
    return redirect('custom_login')