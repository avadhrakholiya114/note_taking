from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Notes


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-3'}),
            'text': forms.Textarea(attrs={'class': 'form-control my-3'})
        }
        labels = {
            'text': 'Write Your Thoughts',
        }

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if 'Django' not in title:
    #         raise forms.ValidationError('we only accept django notess')
    #     return title


class Registerform(UserCreationForm):
    # add additional field
    email = forms.EmailField()

    # meta class is nothing but ptovide info about this class itself
    # hold info about regi...form
    class Meta:
        # ene khaber nathi kaya model ne belong kare so..janavva  mate
        model = User
        # field kay kay avvani e
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control my-3'}),
            'email': forms.EmailInput(attrs={'class': 'form-control my-3'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control my-3'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control my-3'})
        }
